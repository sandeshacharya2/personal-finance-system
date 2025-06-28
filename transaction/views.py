from django.shortcuts import render
from income.models import Income
from expense.models import Expense
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from datetime import datetime

@login_required
def transactions(request):
    user = request.user
    type_filter = request.GET.get('type', 'all')
    search_term = request.GET.get('search', '')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    incomes = Income.objects.filter(user=user)
    expenses = Expense.objects.filter(user=user)

    # Apply search
    if search_term:
        incomes = incomes.filter(source__icontains=search_term)
        expenses = expenses.filter(source__icontains=search_term)

    # Apply date range filter
    if start_date:
        incomes = incomes.filter(date__gte=start_date)
        expenses = expenses.filter(date__gte=start_date)
    if end_date:
        incomes = incomes.filter(date__lte=end_date)
        expenses = expenses.filter(date__lte=end_date)

    # Combine based on type
    if type_filter == 'income':
        transactions = incomes
        for t in transactions:
            t.category = 'income'
    elif type_filter == 'expense':
        transactions = expenses
        for t in transactions:
            t.category = 'expense'
    else:
        # Combine both
        for i in incomes:
            i.category = 'income'
        for e in expenses:
            e.category = 'expense'
        transactions = sorted(
            list(incomes) + list(expenses),
            key=lambda x: x.date,
            reverse=True
        )

    # Paginate
    paginator = Paginator(transactions, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "transactions.html", {
        "page_obj": page_obj,
        "type": type_filter,
        "search_term": search_term,
        "start_date": start_date,
        "end_date": end_date,
    })
