from django.shortcuts import render
from .models import Product
from .forms import ProductForms
from django.http import HttpResponse


def Product_page(request):
    if request.method == "POST":
        form = ProductForms(request.POST, request.FILES) # collecting the data
        if form.is_valid(): # Validating the data
            form.save() # saving the data
            return HttpResponse("product has been created successfully")
    

    else:
        form = ProductForms()
        product = Product.objects.all()


    context = {
        "product" : product,
        "form" : form
    }
    return render(request, "ecommerce/product.html", context)


def product_detail_page(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        "product": product
    }
    return render(request, "ecommerce/detail.html", context)