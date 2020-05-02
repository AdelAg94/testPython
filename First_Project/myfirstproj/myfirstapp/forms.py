from django import forms
from django.core import validators
from .models import PersonProfile
from django.contrib.auth.models import User

class Message(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    veremail = forms.EmailField(label= "Verify Email")
    text = forms.CharField(widget = forms.Textarea)

    def clean(self):
        c_email = self.cleaned_data['email']
        c_veremail = self.cleaned_data['veremail']

        if c_email != c_veremail:
            raise forms.ValidationError("Check if email is correct")

class NewUser(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password","email")

class ExUser(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password")

class ProfileInfo(forms.ModelForm):
    class Meta:
        model = PersonProfile
        exclude = ["user"]