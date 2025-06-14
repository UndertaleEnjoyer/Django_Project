from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.password_validation import password_validators_help_text_html

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mb-3'}))
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control mb-3'}),
    )

class SignupForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mb-3'}))
    password = forms.CharField(
        label='Password',
        strip=False,
        help_text=password_validators_help_text_html(),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3'}),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3'}),
        help_text='Enter the same password as before, for verification.',
    )

    class Meta:
        model = get_user_model()
        fields = ('username',)