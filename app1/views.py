from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import *
from app1.forms import *
# Create your views here.
# def Hello(request):
#     return HttpResponse('<h1>Hello BUdddy!!!!</h1>')

def Check(request):
    form=Creation()
    if request.method == 'POST':
        form=Creation(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'message.html')

    d={'form' : form}
    return render(request,'form.html',d)
def Pow(request):
    met=Question.objects.all()
    d={'met':met}
    return render(request,'index.html',d)