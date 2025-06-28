from django.shortcuts import render, redirect, get_object_or_404
from bills.models import Bill
from bills.forms import BillForm
from django.contrib.auth.decorators import login_required

@login_required
def delete_bill(request, pk):
    bill = get_object_or_404(Bill, pk=pk, user=request.user)
    if request.method == 'POST':
        bill.delete()
        return redirect('bill_list')
    return render(request, 'bills/delete_bill.html', {'bill': bill})