from django.shortcuts import render

from app.models import About


def about_view(request):
    about = About.objects.all()
    return render(request, 'about.html', context={'about': about})
