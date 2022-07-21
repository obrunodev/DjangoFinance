from django.shortcuts import render

from finance.models import Category, Income


# VIEWS DE DASHBOARD
def dashboard_index(request):
    '''Carrega a dashboard'''
    return render(request, 'finance/dashboard/index.html')


# VIEWS DE RENDA MENSAL
def income_index(request):
    '''Renderiza as tabelas de renda da família'''
    income = Income.objects.order_by('day_recurrency')
    context = {'income': income}
    if request.method == 'GET':
        context['total_expected_value'] = sum([item.expected_value for item in income])
        context['total_real_value'] = sum([item.real_value for item in income])
        context['relation'] = context['total_real_value'] - context['total_expected_value']
    return render(request, 'finance/income/index.html', context)


def income_manage(request):
    '''Tela de gestão de rendas'''
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'finance/income/manage.html')
