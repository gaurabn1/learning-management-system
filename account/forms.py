from django import forms

from account.models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']