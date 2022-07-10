from django.shortcuts import render


def index(request):
    return render(request, 'finance/pages/index.html')
