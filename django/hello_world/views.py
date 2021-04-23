from django.shortcuts import render


def index(request):
    """Placeholder index view"""
    params = {'title': 'Hello World Django'}
    return render(request, 'index.html', params)
