from django.shortcuts import get_object_or_404, redirect, render

from ..models import Category


def index(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})


def delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('finance:categories_index')
    else:
        return render(request, 'categories/delete.html', {'category': category})
