from django.shortcuts import redirect, render

from ..forms import CategoryForm
from ..forms import SpendingForm
from ..models import Category
from ..models import Spending


def index(request):
    categories = Category.objects.order_by('name')
    spendings = Spending.objects.all()
    form = SpendingForm()
    return render(request, 'finance/index.html', {
        'categories': categories,
        'form': form,
        'spendings': spendings
    })


def create(request):
    categories = Category.objects.order_by('name')
    spendings = Spending.objects.all()
    if request.method == 'POST':
        form = SpendingForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.difference = obj.expected_cost - obj.real_cost
            category = Category.objects.get(name=obj.category)
            category.total_expected_cost += obj.expected_cost
            category.total_real_cost += obj.real_cost
            category.total_difference += obj.difference
            category.save()
            obj.save()
            return redirect('finance:index')
        return render(request, 'finance/index.html', {
            'categories': categories,
            'form': form,
            'spendings': spendings
        })
