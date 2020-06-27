from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from .functions import (
    save_self_answers_to_db,
    save_relation_answers_to_db,
    find_similar_usernames,
    find_answer_groups_counts,
    get_data_fn,
    return_questions,
    form_json_data
)
from .forms import (
    RelationSelectorForm,
    AnswerFormset
)


class HowtoView(TemplateView):
    template_name = 'interactions/howto_self.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.WARNING,
                'You are not logged in, you will be redirected to login'
            )
        return super().dispatch(request, *args, **kwargs)


class View(PermissionRequiredMixin, TemplateView):
    template_name = 'interactions/view.html'
    permission_required = ('users.special_access',)
    permission_denied_message = 'You do not have the required permissions to access that page'
    raise_exception = True

    def data(self):
        return get_data_fn()


class SelfQuestionView(FormView):
    """ Displays the ``form`` which eventually saves all the answers in the
    database after necessary validation. The function ``return_questions``
    yields a list of questions which is present as a json file present in
    ``docs/project_deps/data/self_questions.json``. After a test is
    successfully attempted, a ``request.session['self_ans_gp']`` is set
    to the Test ID of the newly created test. This can be used for
    notification purposes on the results page. """

    template_name = 'interactions/questions.html'
    form_class = AnswerFormset
    questions = return_questions('SelfAnswerGroup')
    extra_context = {'questions': questions}

    def get_success_url(self):
        url = reverse_lazy(
            'users:results',
            kwargs={'username': self.request.user.username}
        )
        return url

    def form_valid(self, formset):
        json_data = form_json_data(formset, self.questions)
        primary_key = save_self_answers_to_db(
            json_data, self.request
        )
        self.request.session['self_ans_gp'] = primary_key
        messages.add_message(self.request, messages.SUCCESS,
                             'Your answers were saved successfully')
        return super(SelfQuestionView, self).form_valid(formset)

# FIXME: Since both RelationQUestionView and SelfQuestionView are same,
# (with the difference of sending different questions to the view), an
# inheritance BaseClass should be implemented to prevent duplicate code


class RelationQuestionView(FormView):
    """ Same as ``SelfQuestionView`` with the difference that the questions
    sent are loaded from ``docs/project_deps/data/relation_questions.json``.
    A ``request.session['rel_ans_gp']`` set in this case. """
    template_name = 'interactions/questions.html'
    form_class = AnswerFormset
    questions = return_questions('RelationAnswerGroup')
    extra_context = {'questions': questions}

    def get_success_url(self):
        url = reverse_lazy(
            'users:results',
            kwargs={'username': self.request.user.username}
        )
        return url

    def form_valid(self, formset):
        json_data = form_json_data(formset, self.questions)
        primary_key = save_relation_answers_to_db(
            self.kwargs['pk'], json_data, self.request
        )
        self.request.session['rel_ans_gp'] = primary_key
        messages.add_message(self.request, messages.SUCCESS,
                             'Your answers were saved successfully')
        return super(RelationQuestionView, self).form_valid(formset)


@login_required
def howto_relations_view(request):
    if request.method == 'POST':
        form = RelationSelectorForm(request.POST)
        if form.is_valid():
            queryset = find_similar_usernames(form, request)
            answer_groups_counts = find_answer_groups_counts(queryset)
            context = {
                'form': form,
                'queryset': list(zip(queryset, answer_groups_counts))
            }
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
                messages.success(request, 'The requested profile was found!')
                return render(request, 'interactions/howto_relations.html',
                              context)
        else:
            messages.info(request, 'Please correct the errors below ')
    else:
        form = RelationSelectorForm(request.GET or None)
    return render(request, 'interactions/howto_relations.html', {'form': form})
