from django.shortcuts import (
    render,
    redirect,
    HttpResponseRedirect,
)
from django.contrib.auth import authenticate, login,  update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.urls import reverse
from django.views.generic import UpdateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings

from interactions.models import (
    SelfAnswerGroup,
    RelationAnswerGroup
)
from .forms import (
    RegistrationForm,
    ProfileUpdateForm,
    UserUpdateForm
)
from .models import UserProfile
from decorators import check_recaptcha
from mixins import CustomLoginRequiredMixin


@login_required
def result_view(request, username):
    self_answer_groups = SelfAnswerGroup.objects.filter(
        self_user_profile=request.user.profile).order_by('-answer_date_and_time')
    relation_answer_groups = RelationAnswerGroup.objects.filter(
        self_user_profile=request.user.profile).order_by(
            '-answer_date_and_time'
    )
    others_answer_groups = RelationAnswerGroup.objects.filter(
        relation_user_profile=request.user.profile).order_by(
            '-answer_date_and_time'
    )
    return render(
        request, 'users/results.html', {
            'self_answer_groups': self_answer_groups,
            'relation_answer_groups': relation_answer_groups, 
            'others_answer_groups': others_answer_groups
        }
    )


@login_required
def update_profile_view(request, username):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO,
                             'You need to be logged in to edit your profile. ')
    instance = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST, instance=instance)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.add_message(request, messages.INFO,
                                 'Your profile was updated successfully! ')
            url = reverse('users:profile', args=[request.user])
            return redirect(url)
        else:
            messages.add_message(request, messages.INFO,
                                 'Please correct the errors below')

    else:
        profile_form = ProfileUpdateForm(instance=instance)
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/userprofile_form.html', {
        'profile_form': profile_form,
        'user_form': user_form,
    })


@check_recaptcha
def register(request):
    SITE_KEY = settings.GOOGLE_RECAPTCHA_SITE_KEY
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(
                request, 'Your account was activated successfully ')
            return redirect('home:home')
    else:
        form = RegistrationForm()
    return render(
        request, 'users/register.html', {'form': form,
                                         'SITE_KEY': SITE_KEY}
    )


@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was updated successfully! ')
            return redirect(reverse('users:password-change-done'))
        else:
            messages.info(request, 'Please correct the errors below ')
    else:
        form = PasswordChangeForm(request.user)

    print(form.as_p, request.POST)
    return render(request, 'users/password_change_form.html', {'form': form})


class ProfileView(CustomLoginRequiredMixin, DetailView):
    template_name = 'users/profile.html'
    login_url = reverse_lazy('users:login')

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)


class ProfileUpdateView(CustomLoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = UserProfile
    form_class = ProfileUpdateForm


# TODO: Change to FormView CBV
class UserLoginView(auth_views.LoginView):
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        if self.request.user.is_authenticated:
            messages.add_message(request, messages.INFO,
                                 'You are now logged in successfully! ')
        return super().dispatch(request, *args, **kwargs)


class UserPasswordChangeDoneView(
    CustomLoginRequiredMixin, auth_views.PasswordChangeDoneView
):
    template_name = 'users/password_change_done.html'


# TODO: Fix html_email_template.html
class PasswordResetView(auth_views.PasswordResetView):
    success_url = reverse_lazy('users:password-reset-done')
    template_name = 'users/password_reset/password_reset_form.html'
    email_template_name = 'users/password_reset/password_reset_email.html'
    subject_template_name = 'users/password_reset/password_reset_subject.txt'
    html_email_template_name = 'users/password_reset/html_email_template.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'users/password_reset/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'users/password_reset/password_reset_confirm.html'
    success_url = reverse_lazy('users:password-reset-complete')


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'users/password_reset/password_reset_complete.html'


class SelfAnswerGroupsListView(CustomLoginRequiredMixin, ListView):

    def get_queryset(self):
        return SelfAnswerGroup.objects.filter(
            self_user_profile=self.kwargs['pk']
        ).order_by('-answer_date_and_time')
