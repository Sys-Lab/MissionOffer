from django import forms


class LoginForm(forms.Form):
    usrname = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    pass