from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from users.models import User


class UserForm(UserChangeForm):
    """Форма для профиля пользователя"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserRegisterForm(UserCreationForm):
    """Форма для регистрации пользователя"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'phone', 'avatar')