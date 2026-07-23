from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    query = request.GET.get("q", "")
    if query:
        products = products.filter(name__icontains=query)
    return render(
        request,
        "products/list.html",
        {"products": products, "categories": categories, "query": query},
    )


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    categories = Category.objects.all()
    return render(
        request,
        "products/list.html",
        {"products": products, "categories": categories, "category": category},
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "products/detail.html", {"product": product})


def new(request):
    from django.http import HttpResponse

    return HttpResponse("Hello, New.")
