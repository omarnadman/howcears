from django.shortcuts import render
from .models import Person
from django.core.mail import send_mail



def home(request):

    return render(request , 'home.html')



def singup(request):
    person = Person.objects.all()
    f_name = request.POST.get('first_name')
    l_name = request.POST.get('last_name')
    email = request.POST.get('email')
    number = request.POST.get('number')
    zip = request.POST.get('zip')
    if request.POST.get ('submit'):
        person.create(first_name=f_name ,last_name=l_name ,email=email ,number=number,zip=zip)

        send_mail(
            f_name,
            'some thing',
            email,
            ['omarnadman@gmail.com'],
        )
    return render(request, 'singup.html', {'person':person})

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def page4(request):
    return render(request, 'page4.html')