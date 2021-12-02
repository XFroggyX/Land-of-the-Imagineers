from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()


class UsersRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fields = ['username', 'password1', 'password2', 'email']

