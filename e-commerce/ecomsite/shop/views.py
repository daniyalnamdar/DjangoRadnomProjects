from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    productObjects = Product.objects.all()

    # Search Code
    itemName = request.GET.get('item_name')
    if itemName != '' and itemName is not None:
        productObjects = productObjects.filter(title__icontains=itemName)


    # Paginator 
    paginator = Paginator(productObjects, 4)
    page = request.GET.get('page')
    productObjects = paginator.get_page(page)
    
    return render(request, 'shop/index.html', {'productObjects': productObjects})


def detail(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'shop/detail.html', {'product': product})


def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")

        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()

    return render(request, 'shop/checkout.html')