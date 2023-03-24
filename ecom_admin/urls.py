from django.urls import path
from . import views 
app_name='ecom_admin'

urlpatterns=[
  path('home',views.home),
  path('approveseller',views.approveseller,name='approveseller'),
  path('viewseller',views.viewseller),
  path('viewcustomer',views.viewcustomer),
  path('viewproduct',views.view_product,name='view_product'),
  
]
