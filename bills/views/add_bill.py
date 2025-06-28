from django.shortcuts import render, redirect, get_object_or_404
from bills.models import Bill
from bills.forms import BillForm
from django.contrib.auth.decorators import login_required

@login_required
def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST, request.FILES)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.user = request.user
            bill.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'bills/add_bill.html', {'form': form})

