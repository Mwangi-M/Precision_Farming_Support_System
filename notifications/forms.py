from django import forms
from .models import Notifications

# Create your models here.
class PostForm(forms.ModelForm):

    class Meta:
        model = Notifications
        fields = ['message', 'image']
