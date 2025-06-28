
from django.shortcuts import render, redirect, get_object_or_404
from bills.models import Bill
from bills.forms import BillForm
from django.contrib.auth.decorators import login_required

@login_required
def bill_list(request):
    bills = Bill.objects.filter(user=request.user)
    return render(request, 'bills/bill_list.html', {'bills': bills})

# # bills/views.py
# from django.shortcuts import render, get_object_or_404
# from .models import Bill
@login_required
def bill_detail(request, pk):
    bill = get_object_or_404(Bill, pk=pk, user=request.user)
    return render(request, 'bills/bill_detail.html', {'bill': bill})
