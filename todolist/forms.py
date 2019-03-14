from django import forms
from .models import *

class TodoForm(forms.ModelForm):
	content = forms.CharField(label="",widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter todo list item','rows':'1',}))
	class Meta:
 		model = Todo
 		fields = ['content','date','time']
