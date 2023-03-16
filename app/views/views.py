from django.shortcuts import render


def index_view(request):
    """Стартовая страница"""
    return render(request, 'index.html')
