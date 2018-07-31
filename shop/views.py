from django.shortcuts import render
from .models import *
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import BuyProductForm
from django.contrib.auth.decorators import login_required
from functools import reduce
# Create your views here.
def index(request):
    num_brands=Brand.objects.all().count()
    num_categories=Category.objects.all().count()
    num_products=Product.objects.all().count()
    context={
        'num_brands':num_brands,
        'num_categories':num_categories,
        'num_products':num_products,
    }
    return render(request,'index.html',context=context)

class BrandListView(generic.ListView):
    model=Brand
    paginate_by=10

class CategoryListView(generic.ListView):
    model=Category
    paginate_by=10

class BrandDetailView(generic.DetailView):
    model=Brand

class CategoryDetailView(generic.DetailView):
    model=Category

class ProductDetailView(generic.DetailView):
    model=Product

@login_required()
def BuyProductView(request,pk):
    pr=get_object_or_404(Product,pk=pk)
    if(request.method=='POST'):
       form=BuyProductForm(request.POST)
       if form.is_valid():
            qty=form.cleaned_data['quantity']
            if pr.inventory >= qty and qty>0:
                pr.inventory=pr.inventory - qty
                pr.save()
                ci=CartItem.objects.filter(product=pr,user=request.user)
                if(ci.count()>0):
                    ci2=ci[0]
                    ci2.quantity+=qty
                    ci2.save()
                else :
                    ci=CartItem(product=pr,user=request.user,quantity=qty)
                    ci.save()
                return HttpResponseRedirect(reverse('cart'))
            else:
                return(render(request,'shop/buy_product.html',{
                    'form':BuyProductForm(),
                    'product_name':pr.name,
                    'error_inventory':str(pr.inventory),
                }))
    else:
        form=BuyProductForm(initial={'1':pr.inventory,})
    return render(request,'shop/buy_product.html',{'form':form, 'product_name':pr.name})

@login_required()
def CartView(request):
    items=request.user.cartitem_set.all()
    grand_total=sum([x.total_price for x in items])
    return render(request,'shop/cart.html',context={
        'items':items,
        'grand_total':grand_total,
    })
