from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib import messages


class CustomLoginRequiredMixin(LoginRequiredMixin):

    permission_denied_message = 'You have to be logged in to access that page'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.WARNING,
                                 self.permission_denied_message)
            return self.handle_no_permission()
        return super(CustomLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class RequiredFieldsMixin:

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        required_fields = getattr(self.Meta, 'required_fields', None)

        if required_fields:
            if required_fields == '__all__':
                for key in self.fields:
                    self.fields[key].required = True
            for key in self.fields:
                if key in required_fields:
                    self.fields[key].required = True
