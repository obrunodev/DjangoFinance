from django.shortcuts import render


def index(request):
    return render(request, 'core/pages/index.html')


def create(request):
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        pass


def update(request, pk):
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        pass


def delete(request, pk):
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        pass
