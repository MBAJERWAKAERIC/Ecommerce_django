from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . models import Product

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

class CategoryView(View):
    def get(self, request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title') 
        return render(request, 'app/category.html', locals())


class CategoryTitle(View):
    def get(self, request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title').annotate(total=Count('title'))
        return render(request, 'app/category.html', locals())

class ProductDetail(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', locals())