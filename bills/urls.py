from django.urls import path
from . import views
from bills.views import add_bill, bill_list, update_bill, delete_bill


urlpatterns = [
    
    path('', views.bill_list, name='bill_list'),
    path('add/', views.add_bill, name='add_bill'),
    path('update/<int:pk>/', views.update_bill, name='update_bill'),
    path('delete/<int:pk>/', views.delete_bill, name='delete_bill'),
   path('<int:pk>/', views.bill_detail, name='bill_detail'),
     
]
