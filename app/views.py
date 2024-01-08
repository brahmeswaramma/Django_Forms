from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Data is Inserted')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=="POST":
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()
            return HttpResponse('Webpage_Data is Inserted') 
        else:
            return HttpResponse('Invalid Data') 
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EARFO=AccessRecord_Form()
    d={'EARFO':EARFO}
    if request.method=="POST":
        ARFDO=AccessRecord_Form(request.POST)
        if ARFDO.is_valid():
            n=ARFDO.cleaned_data['name']
            WO=Webpage.objects.get(name=n)
            d=ARFDO.cleaned_data['date']
            a=ARFDO.cleaned_data['author']
            ARO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
            ARO.save()
            return HttpResponse('AccessRecord_Data is Inserted')             
        else:
            return HttpResponse('Invalid Data') 
    return render(request,'insert_accessrecord.html',d)


