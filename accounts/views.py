from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def home(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form=UserCreationForm()
    context={
    'form':form
    }
    return render(request,'accounts/home.html',context)
