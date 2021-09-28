from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import *

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()

		return user


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'name', 'location', 'profile_pic', 'neighborhood')