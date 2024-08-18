from django import forms

REGISTER_ATTRS = {'class': 'form-control border-2'}


class CommentForm(forms.Form):
	text = forms.CharField(
		widget=forms.TextInput(
			attrs={"class": "form-control border border-2"}),
		max_length=100,
		required=True,
		help_text="Напишу-ка я...",
	)


class RegisterUserForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(REGISTER_ATTRS),
		max_length=100
	)
	email = forms.EmailField(
		widget=forms.EmailInput(REGISTER_ATTRS),
		max_length=100,
		required=False,
		help_text="Ваш email..",

	)
	password = forms.CharField(
		max_length=100,
		widget=forms.PasswordInput(REGISTER_ATTRS)
	)

	fullname = forms.CharField(
		widget=forms.TextInput(REGISTER_ATTRS),
		max_length=100,
		required=False
	)

	birthdate = forms.DateField(
		widget=forms.SelectDateWidget(REGISTER_ATTRS)
	)

	about = forms.CharField(
		widget=forms.Textarea(attrs={'class': 'form-control border-2', 'style': 'height: 130px'})
	)

	def __init__(self, *args, **kwargs):
		super(forms.Form, self).__init__(*args, **kwargs)
		self.fields['email'].label = "Электронная почта:"
		self.fields['username'].label = "Имя пользователя:"
		self.fields['password'].label = "Пароль:"
		self.fields['fullname'].label = "Полное имя:"
		self.fields['birthdate'].label = "Дата рождения:"
		self.fields['about'].label = "Немного о вас:"


class LoginUserForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(REGISTER_ATTRS),
		max_length=100
	)
	password = forms.CharField(
		max_length=100,
		widget=forms.PasswordInput(REGISTER_ATTRS)
	)

	def __init__(self, *args, **kwargs):
		super(forms.Form, self).__init__(*args, **kwargs)
		self.fields['username'].label = "Имя пользователя:"
		self.fields['password'].label = "Пароль:"
