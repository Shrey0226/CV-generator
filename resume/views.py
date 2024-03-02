from django.shortcuts import render, redirect
from .models import user
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.


def Home(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        adress = request.POST.get("adress", "")
        Degree = request.POST.get("Degree", "")
        university = request.POST.get("university", "")
        duration = request.POST.get("duration", "")
        summary = request.POST.get("summary", "")
        projects = request.POST.get("projects", "")
        skills = request.POST.get("skills", "")
        work = request.POST.get("work", "")
        achivement = request.POST.get("achivement", "")
        links = request.POST.get("skills", "")
        User = user(name=name, email=email, phone=phone, adress=adress, Degree=Degree, university=university,
                    duration=duration, summary=summary, skills=skills, projects=projects, work=work, achivement=achivement, links=links)
        User.save()
    return render(request, 'resume/home.html')


def download(request, id):
    user_data = user.objects.get(pk=id)
    template = loader.get_template('resume/cv.html')
    html = template.render({'user_data': user_data})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    config = pdfkit.configuration(
        wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(
        html, False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename=resume.pdf'

    return response


def user_list(request):
    users = user.objects.all()
    return render(request, 'resume/list.html', {'users': users})
