from django.shortcuts import render ,redirect
from common.models import seller
from seller.models import Product

# Create your views here.

def home(request):
    return render(request,'ecom_admin/home.html')

def approveseller(request):
    
    if request.method == 'POST':
        pid =request.POST['sid']
        if 'btn_approve' in request.POST:
            seller.objects.filter(id=pid).update(action='Approved')

        if 'btn_reject' in request.POST:
            seller.objects.filter(id=pid).update(action='Reject')
         
    seller_details =seller.objects.filter(action='Pending')
    return render(request,'ecom_admin/approve seller.html',{'seller_details': seller_details})
   
def viewcustomer(request):
    return render(request,'ecom_admin/view customer.html')  

def viewseller(request):
    return render(request,'ecom_admin/view seller.html')  

def view_product(request):
    all_product =Product.objects.all()

    return render(request,'ecom_admin/view_product.html',{'all_product':all_product})   

# def rejectseller(request,sid):
#     seller_details =seller.objects.all()
#     print(sid)
    
#     return render(request,'ecom_admin/approve seller.html')