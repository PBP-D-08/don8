from django import forms
from authentication.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password1 = forms.CharField(
        label="Password", max_length=100, widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password", max_length=100, widget=forms.PasswordInput
    )
    role = forms.ChoiceField(
        label="Role", choices=[("user", "Pengguna"), ("company", "Perusahaan")]
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get("username")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # check if username exist
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exist")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
