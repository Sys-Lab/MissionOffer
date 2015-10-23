from django import forms


class LoginForm(forms.Form):
    UN = forms.CharField()
    PW = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    pass