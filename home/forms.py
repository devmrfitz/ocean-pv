from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        required=True,
        label='Email ID',
        widget=forms.TextInput(
            attrs={'placeholder': 'Please enter your Email ID here (required)'}
        )
    )
    subject = forms.CharField(
        required=True,
        label='Email Subject',
        widget=forms.Textarea(
            attrs={'placeholder': 'Please enter the Email subject (optional)'}
        )
    )
    message = forms.CharField(
        required=True,
        label='Email Body', 
        widget=forms.Textarea(
            attrs={'placeholder': 'Please enter the message you want to send (required)'}
        )
    )

    def send_email(self, *args, **kwargs):
        from_email = self.cleaned_data.get('from_email')
        subject = self.cleaned_data.get('subject')
        message = self.cleaned_data.get('message')

        send_mail(
            subject=subject.strip(),
            message=message,
            from_email=from_email.strip(),
            recipient_list=[settings.EMAIL_HOST_USER] if settings.EMAIL_HOST_USER else ['ocean-pv_dev@email.com'], 
            fail_silently=False, 
        )
