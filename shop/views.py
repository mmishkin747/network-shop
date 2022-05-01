from django.http import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Category, Product , MainCatigory
from cart.forms import CartAddProductForm

def index(request):
    return render(
        request,
        'shop/index.html',
        {},
    )

def product_list(request, category_slug=None):
    category = None
    main_category = MainCatigory.objects.all()
    
    categories = []
    for mc in main_category:
        c = Category.objects.filter(main_category__name=mc.name)
        categories.append([mc.name, c])

  
    products = Product.objects.filter(available=True)
    #print(Category.objects.get(main_category_id=2))

    test_dt = [1, 2, 3]

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    return render(request,
                  'shop/product/list.html',
                  {
                    'category': category,
                   'categories': categories,
                   'products': products
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form})
