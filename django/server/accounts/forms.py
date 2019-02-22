from django import forms
from .models import AccountUser


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, 
        max_length=128
    )
    password = forms.CharField(
        required=True, 
        max_length=72,
        widget=forms.widgets.PasswordInput()
    )


class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(
        required=True,
        max_length=72,
        widget=forms.widgets.PasswordInput()
    )

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password is not confirm')

        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        password = self.cleaned_data.get('password')

        user.set_password(password)

        if commit:
            user.save()

        return user

    class Meta:
        model = AccountUser
        fields = ['username', 'password']
        widgets = {
            'password': forms.widgets.PasswordInput()
        }
