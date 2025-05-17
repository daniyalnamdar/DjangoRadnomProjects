from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


def index(request):
    items = Item.objects.all()
    context = {'items': items,}
    return render(request, 'food/index.html', context)


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'


def item(request):
    return HttpResponse('this is an item.')

def detail(request, id):
    item = Item.objects.get(pk=id)
    context = {'item': item,}
    return render(request, 'food/detail.html', context)


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
 

class CreateItem(CreateView):
    model =Item
    fields = ['name', 'description', 'price', 'image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    



def createItem(request):
    form  = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form})

def updateItem(request, id):
    item = Item.objects.get(pk=id)
    form  = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form, 'item': item})

def deleteItem(request, id):
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html',{'item': item})