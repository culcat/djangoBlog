from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from djangoApplication.models import *
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'content')


class DeleteForm(forms.Form):
    post_id = forms.IntegerField()

class EditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'content')