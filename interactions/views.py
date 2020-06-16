from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView, ListView, FormView
from django.contrib.auth.models import User

from .functions import (
    save_self_answers_to_db,
    save_relation_answers_to_db
)
from .models import (
    SelfQuestion,
    UserAnswerChoice,
    SelfAnswerGroup,
    RelationQuestion,
    RelationAnswerGroup,
    RelationAnswerChoice
)
from .forms import (
    UserAnswerChoiceForm,
    RelationSelectorForm
)
from mixins import CustomLoginRequiredMixin 


class HowtoView(TemplateView):
    template_name = 'interactions/howto_self.html'

@login_required
def self_question_list_view(request):
    questions = [question['question_text']
                 for question in SelfQuestion.objects.values('question_text')]
    if not questions:
        return render(request, 'interactions/error.html')
    if request.method == 'POST':
        form = UserAnswerChoiceForm(request.POST)
        if form.is_valid():
            new_answer_group_pk = save_self_answers_to_db(
                request.user,
                form,
                len(questions)
            )
            request.session['answer_group'] = new_answer_group_pk
            messages.success(
                request, 'Your password was updated successfully! ')
            return redirect('users:results', username=request.user.username)
        else:
            messages.info(request, 'Please correct the errors below ')
    else:
        form = UserAnswerChoiceForm()

    return render(request, 'interactions/questions.html', {'form': zip(form, questions)})


@login_required
def relation_question_list_view(request, pk):
    questions = [question['question_text']
                 for question in RelationQuestion.objects.values('question_text')]
    if not questions:
        return render(request, 'interactions/error.html')
    if request.method == 'POST':
        form = UserAnswerChoiceForm(request.POST)
        if form.is_valid():
            new_answer_group_pk = save_relation_answers_to_db(
                request.user,
                pk,
                form,
                len(questions)
            )
            request.session['relation_answer_group'] = new_answer_group_pk
            messages.success(
                request, 'Your password was updated successfully! ')
            return redirect('users:results', username=request.user.username)
        else:
            messages.info(request, 'Please correct the errors below ')
    else:
        form = UserAnswerChoiceForm()

    return render(request, 'interactions/questions.html', {'form': zip(form, questions)})


class HowtoViewRelations(CustomLoginRequiredMixin, FormView):
    form_class = RelationSelectorForm
    template_name = 'interactions/howto_relations.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username').strip()
        profile = self.request.user.profile
        try:
            self.profile = User.objects.get(username=username).profile.pk
        except ObjectDoesNotExist:
            messages.add_message(self.request, messages.INFO,
                                 "The requested user does not exist")
            self.profile = None
        return super().form_valid(form)

    def get_success_url(self):
        if self.profile:
            url = reverse('interactions:taketest-relations',
                          kwargs={'pk': self.profile})
            self.success_url = url
        else:
            url = reverse('interactions:howto-relations')
            self.success_url = url
        return super().get_success_url()

    def form_invalid(self, form):
        messages.add_message(self.request, messages.INFO,
                             "Please correct the errors below")
        return super().form_invalid(form)
