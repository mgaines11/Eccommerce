from django.shortcuts import render

# Create your views here.

from .models import Category, Product


def all_products(request):
        # line of code below is a query. Selectall in SQL basically. Saving all data from the data base into the products Variable
        products = Product.objects.all()
       # now to make that data availale on the template so we return it.
        return render(request, 'store/home.html', {'products': products})
       # in django render is used for loading the templates. basically a template shortcut.

# return render() - key parameters for render
# return render(url request by user, template, data)