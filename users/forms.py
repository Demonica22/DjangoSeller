from django.contrib.auth.forms import forms
from django.core.validators import EmailValidator
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.validators import validate_international_phonenumber

from .models import User


class UserLoginForm(forms.Form):
    email = forms.CharField(validators=[EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'mobile', 'password', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    mobile = PhoneNumberField(validators=[validate_international_phonenumber])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobile']
