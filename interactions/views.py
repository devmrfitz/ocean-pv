from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView, ListView, FormView
from django.contrib.auth.models import User

from .functions import (
    save_self_answers_to_db,
    save_relation_answers_to_db,
    find_similar_usernames,
    find_answer_groups_counts
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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.WARNING, 'Since you are not logged in, you will be redirected to the login page ')
        return super().dispatch(request, *args, **kwargs)


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
                request, 'Your answers were saved successfully! ')
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
                request, 'Your answers were saved successfully! ')
            return redirect('users:results', username=request.user.username)
        else:
            messages.info(request, 'Please correct the errors below ')
    else:
        form = UserAnswerChoiceForm()

    return render(request, 'interactions/questions.html', {'form': zip(form, questions)})

# TODO: queryset must not show current user's profile in the queryset


@login_required
def howto_relations_view(request):
    if request.method == 'POST':
        form = RelationSelectorForm(request.POST)
        if form.is_valid():
            queryset = find_similar_usernames(form)
            answer_groups_counts = find_answer_groups_counts(queryset)
            context = {'form': form, 'queryset': zip(
                queryset, answer_groups_counts)}
            if not queryset:
                messages.info(request, 'No such profile exists')
                return render(request, 'interactions/howto_relations.html',
                              context)
            if len(queryset) > 1:
                messages.info(
                    request, 'There are multiple profiles with that username')
                return render(request, 'interactions/howto_relations.html',
                              context)
            if len(queryset) == 1:
                profile = queryset.first().pk
                messages.success(request, 'The requested profile was found!')
                return render(request, 'interactions/howto_relations.html',
                              context)
        else:
            messages.info(request, 'Please correct the errors below ')
    else:
        form = RelationSelectorForm(request.GET or None)
    return render(request, 'interactions/howto_relations.html', {'form': form})
