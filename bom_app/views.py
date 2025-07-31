from django.shortcuts import render, get_object_or_404
from .models import Product, BOMItem

# Create your views here.
def index(request):
    """
    Render the index page.
    """
    products = Product.objects.all()
    return render(request, 'bom_app/index.html', {'products': products})

def bom_view(request, product_id):
    """
    Render the Bill of Materials page.
    """
    product = get_object_or_404(Product, id=product_id)
    bom = product.get_bom_tree()
    context = {
        'product': product,
        'bom': bom,
    }
    return render(request, 'bom_app/bom_view.html', context)