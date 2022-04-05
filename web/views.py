import email
from django.shortcuts import render
from .models import Person
from django.core.mail import send_mail
from .forms import Send



def home(request):

    return render(request , 'home.html')



def singup(request):
    form = Send()
    submitted = False
    if request.method == "POST":
        form = Send(request.POST)
        if form.is_valid():
            form.save()

            send_mail(
                Person.first_name,
                'some thing',
                Person.email,
                ['omarnadman@gmail.com'],
            )
    return render(request, 'singup.html', {'for':form})

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def page4(request):
    return render(request, 'page4.html')