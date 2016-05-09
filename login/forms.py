from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class login_form(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

class register_form(forms.ModelForm):
	password2 = forms.CharField()
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required = True)
	last_name = forms.CharField(required = True)
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'email','password','password2']

	def clean(self):
		cleaned_data = super(register_form,self).clean()
		password = cleaned_data.get("password")
		password2 = cleaned_data.get('password2')

		if password and password2 and password2 == password :
			return cleaned_data
		else :
			raise forms.ValidationError(_("password does not match."))


