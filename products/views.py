from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.models import Product, ProductCategory, Basket


def index(request):
    context = {
        'title': 'Clothes',
    }
    return render(
        request,
        'products/index.html',
        context
    )


def products(request, category_id=None, page_number=1):

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Clothes - Каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),

    }
    return render(
        request,
        'products/products.html',
        context
    )


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])