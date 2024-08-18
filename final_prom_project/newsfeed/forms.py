from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control border border-2"}),
        max_length=100,
        required=True,
        help_text="Напишу-ка я...",
    )


class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        max_length=100,
        required=False,
        help_text="Ваш email..",

    )
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
