from django import forms
from .models import Image, Editor, Comment, Profile

class SubscribeForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['editor', 'pub_date']
        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }



class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'comment_body',}


class updateProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=30,label='Username')
    profile_photo = forms.ImageField(label='Profile picture')
    bio = forms.CharField(label='About you', max_length=200)
