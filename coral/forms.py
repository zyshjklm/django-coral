from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(
		required = True,
		lable = "username",
		error_message = {'required': 'Please enter email address/username'},
		widget=forms.TextInput(
			attrs = {
				'placeholder': u"username",
			}
		),

	)
	password = forms.CharField(
		required = True,
		lable = "password",
		error_message = {'required': 'Enter your password'},
		widget=forms.TextInput(
			attrs = {
				'placeholder': u"username",
			}
		),

	)

