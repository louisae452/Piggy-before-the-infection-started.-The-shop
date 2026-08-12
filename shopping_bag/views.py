
import sys
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product

# Create your views here.
# View to render shopping bag page.
def shopping_bag(request):
    return render(
        request,
        "shopping_bag/shopping_bag.html",
    )
    
def add_to_bag(request, product_code):
    product = get_object_or_404(Product, code=product_code)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    # Create or bring up bag
    bag = request.session.get('bag', {})
    if bag is None:
        bag = {}
    # Add quantity of product to bag.
    if product_code in list(bag.keys()):
        bag[product_code] += quantity
    else:
        bag[product_code] = quantity
    # Update bag.
    request.session['bag'] = bag
    # Test
    # 2. Add flush=True directly inside print
    print("🚨 TEST PRINT - BAG STATUS:", request.session['bag'], flush=True)
    
    # 3. Force system standard output stream to clear out
    sys.stdout.flush() 
    
    
    
    
    
    return redirect(redirect_url)
    
    
        