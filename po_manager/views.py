from django.shortcuts import render
from company_manager import models as company_manager_models
from . import models as po_models
import datetime

# Create your views here.
def list(request):
    return render(request, 'po_manager/list-po.html')

def new(request):
    if request.method == 'POST': 
        # save the form
        # try:
        start_date=datetime.datetime.strptime(
            request.POST.get('start_date'),
            "%Y-%m-%d"
        )
        end_date=datetime.datetime.strptime(
            request.POST.get('end_date'),
            "%Y-%m-%d"
        ) 
        company_id = request.POST.get('company_id')
        company = company_manager_models.Company.objects.get(id=company_id)           
        new_po = po_models.PurchaseOrder.objects.create(
            company_id=company,
            description=request.POST.get('description'),
            amount=float(request.POST.get('amount')),
            start_date=start_date,
            end_date=end_date
        )

        new_po.save()
        message = 'The purchase order has been saved.' 
        #except: 
        #    message = 'Error saving the purchase order.'
    else: 
        message = ''
    companies = company_manager_models.Company.objects.all().order_by('name')
    data = {
        'companies': companies, 
        'message': message
    }
    print(data)
    return render(request, 'po_manager/new-po.html', data)   

def view(request, id):
    print(id)
    return render(request, 'po_manager/view-po.html', {'id': id})     