# coding: utf-8
import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-block-level'
            field.widget.attrs['placeholder'] = field.label


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs = {
        #    'class': 'input-block-level',
        #    'placeholder': self.fields['username'].label,
        #}
        #self.fields['password'].widget.attrs = {
        #    'class': 'input-block-level',
        #    'placeholder': self.fields['password'].label,
        #}
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-block-level'
            field.widget.attrs['placeholder'] = field.label


class RegisterForm(forms.ModelForm):
#class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-block-level'
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', )

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(u'^20[0-9]{6}$', username):  # 20091234
            raise forms.ValidationError('学号只能是数字，长度8位')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('必填项')
        return email

    def clean_password(self):
        return make_password(self.cleaned_data['password'])

    def save(self, commit=True):
        """
        这里commit不能用了。。。
        """
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user

