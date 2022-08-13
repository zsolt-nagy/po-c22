from django.urls import path 
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('new/', views.new, name='new'),
    path('view/<int:id>', views.view, name='view'), # TODO: fix this 
]