from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from myportfolio.models import hobby, personal_info, service , skills , team

#Create your views here:
def index(request):
    my_info=personal_info.objects.get(id=1)
    my_service=service.objects.all()
    my_hobby=hobby.objects.all()
    my_skills = skills.objects.all()
    my_teams = team.objects.all()



    context={
        'personal_infos':my_info,
        'services':my_service,
        'hobby':my_hobby,
        'skills':my_skills,
        'teams':my_teams,
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'index.html', context)


def message_meView(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    email_body=name+', '+ email+ ', ' + message
    sender=settings.EMAIL_HOST_USER
    receivers=['adibarmanshuvro89@gmail.com']

    send_mail(subject, email_body, sender, receivers)

    return HttpResponseRedirect('http://127.0.0.1:8000/#contact')




