"""
COMPANY TABLE 
Company Name:
Company ID:

PO TABLE
Date:
Company ID:
PO #: this is the id

PO ITEMS TABLE 
PO# 
Item Part #:
Item Description:
Qty:
Cost per Item:
"""

from django.urls import path 
from . import views

urlpatterns = [
    path('list/', views.list, name='list-po'),
    path('new/', views.new, name='new-po'),
    path('view/<int:id>', views.view, name='view-po'), 
]