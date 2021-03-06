from django import forms
from hicap.membership.models import Maker

class MakerAuthForm(forms.Form):
	username = forms.fields.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Username"}))
	password = forms.fields.CharField(widget=forms.widgets.PasswordInput(attrs={"placeholder": "Password"}))
