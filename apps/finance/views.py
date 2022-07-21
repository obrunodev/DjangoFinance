from django.shortcuts import render

from finance.models import Income


def dashboard_index(request):
    '''Carrega a dashboard'''
    return render(request, 'finance/dashboard/index.html')


def income_index(request):
    '''Renderiza as tabelas de renda da família'''
    income = Income.objects.order_by('day_recurrency')
    context = {'income': income}
    if request.method == 'GET':
        context['total_expected_value'] = sum([item.expected_value for item in income])
        context['total_real_value'] = sum([item.real_value for item in income])
        context['relation'] = context['total_expected_value'] - context['total_real_value']
    return render(request, 'finance/income/index.html', context)
