from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to plantpot Home!")

# Create your views here.

from .models import product 

def creatproduct(request):

    if request.method == 'POST': #caps must be uppercase
        title = request.POST.get('title') #name on html form
        price = request.POST.get('price')


        product = product(title=title, price=price)  #title 1 is from model  || title 2 is from html form
        product.save()

        
        # Redirect to a success page or render a template
    return render(request, 'plant.html') #return render(request, 'plant.html', {'product': product})
    # return HttpResponse("Product created successfully!")
    
