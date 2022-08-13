from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'po_manager/list-po.html')

def new(request):
    return render(request, 'po_manager/new-po.html')   

def view(request, id):
    print(id)
    return render(request, 'po_manager/view-po.html', {'id': id})     