from django.shortcuts import render, redirect, get_object_or_404
from bills.models import Bill
from bills.forms import BillForm
from django.contrib.auth.decorators import login_required

@login_required
def update_bill(request, pk):
    bill = get_object_or_404(Bill, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BillForm(request.POST, request.FILES, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm(instance=bill)
    return render(request, 'bills/update_bill.html', {'form': form})
