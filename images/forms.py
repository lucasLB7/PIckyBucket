from django import forms
from .models import Image

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