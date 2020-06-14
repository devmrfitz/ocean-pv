from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.contrib.auth.admin import User
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from interactions.functions import save_answers_to_db
from interactions.models import (
    SelfQuestion,
    UserAnswerChoice,
    SelfAnswerGroup,
    RelationQuestion,
    RelationAnswerGroup,
    RelationAnswerChoice
)
from interactions.forms import (
    UserAnswerChoiceForm,
)


# TODO: Convert to func based
class HowtoView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        print(request.get_full_path().split('?next=')[-1])
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
            new_answer_group_pk = save_answers_to_db(
                SelfAnswerGroup,
                UserAnswerChoice,
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
def relation_question_list_view(request):
    questions = [question['question_text']
                 for question in RelationQuestion.objects.values('question_text')]
    if not questions:
        return render(request, 'interactions/error.html')
    if request.method == 'POST':
        form = UserAnswerChoiceForm(request.POST)
        if form.is_valid():
            new_answer_group_pk = save_answers_to_db(
                RelationAnswerGroup,
                RelationAnswerChoice,
                request.user,
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
