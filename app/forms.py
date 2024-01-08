from django import forms
from app.models import *

class TopicForm(forms.Form):
    topic_name=forms.CharField()

class WebpageForm(forms.Form):
    tn=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=tn)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()


class AccessRecord_Form(forms.Form):
    nl=[[wo.name,wo.name] for wo in Webpage.objects.all()]
    name=forms.ChoiceField(choices=nl)
    date=forms.DateField()
    author=forms.CharField()    
