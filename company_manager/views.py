from django.shortcuts import render 
from . import models

# Create your views here.
def list(request):
    companies = models.Company.objects.all().order_by('name')
    data = {
        'companies': companies
    }
    return render(request, 'company_manager/list-companies.html', data)

def new(request):
    if request.method == 'POST':
        # save the form
        try:
            new_company = models.Company(
                    name=request.POST.get('company_name')
                )
            new_company.save()
            message = 'The company has been created'
        except:
            message = 'Error saving company. Please try again later.'
    else: # if request.method == 'GET'
        message = ''
    data = {
        'message': message
    }
    return render(request, 'company_manager/new-company.html', data)   

def view(request, id):
    company = models.Company.objects.get(id=id)
    data = {
        'company': company
    }
    return render(request, 'company_manager/view-company.html', data)  