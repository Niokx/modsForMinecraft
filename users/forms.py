from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import ClearableFileInput
from .models import Profile
from crispy_forms.helper import FormHelper


class CustomClearableFileInput(ClearableFileInput):
    def get_context(self, name, value, attrs):
        value.name = path.basename(value.name)
        context = super().get_context(name, value, attrs)
        return context


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.RegexField(
        label='Username',
        max_length=16,
        regex=r'^[\w-]+$',
        help_text='Your username must contain only letters, numbers, hyphens and underscores.')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.RegexField(
        label='Username',
        max_length=16,
        regex=r'^[\w-]+$',
        help_text='Your username must contain only letters, numbers, hyphens and underscores.')
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'image': forms.FileInput(),
        }
