from django.urls import path
from . import views 
app_name='lightapi'

urlpatterns=[
  path('lightapi',views.add_student),
  path('getstudents',views.view_student),
  path('delete_student/<int:sid>',views.delete_student),
  path('update_student/<int:sid>',views.update_student),
  
  
]
