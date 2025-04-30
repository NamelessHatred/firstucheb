from django.shortcuts import render

def home(request):
    return render(request, 'shop/home.html')

def about(request):
    return render(request, 'shop/about.html')

def contacts(request):
    return render(request, 'shop/contacts.html')

def find_us(request):
    return render(request, 'shop/find_us.html')

def products(request):
    return render(request, 'shop/products.html')

def categories(request):
    return render(request, 'shop/categories.html')

def all_products(request):
    return render(request, 'shop/all_products.html')

def cart(request):
    return render(request, 'shop/cart.html')

