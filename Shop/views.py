from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import *


def home(request):
    products = Product.objects.all()
    search = request.GET.get('search')
    category = request.GET.get('category')
    subcategory = request.GET.get('subcategory')
    categories = Category.objects.all()
    subcategory = request.GET.get('subcategory')
    product_id = request.GET.get('product')
    if product_id:
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem.objects.filter(product=product, customer=request.user)

        if not cart_item:
            CartItem.objects.create(
                customer=request.user,
                product=product,
                quantity=1
            )
            return redirect('shop:home')

        for item in cart_item:
            item.quantity += 1
            item.save()
    products = products.filter(category=category) if category else products
    products = products.filter(subcategory=subcategory) if subcategory else products
    products = products.filter(
        Q(name__iregex=search) | Q(category__name__iregex=search) | Q(
            subcategory__name__iregex=search)) if search else products

    return render(request, 'home.html', {'products': products, 'categories': categories})


def create(request):
    form = BaseForm(request.POST, request.FILES)
    image_form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            product = Product.objects.create(seller=request.user, **form.cleaned_data)
            if image_form.is_valid():
                a = image_form.save(commit=False)
                a.product = product
                a.save()
            return redirect('shop:home')
    return render(request, 'create_product.html', {'form': form, 'form2': image_form})


def detail(request, pk):
    product = Product.objects.get(pk=pk)
    images = Image.objects.filter(product=product)
    if request.method == 'POST':
        return redirect('shop:detail', product.pk)
    return render(request, 'detail.html', {'images': images, 'product': product})


def reklama(request):
    return render(request, 'reklama.html')


def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    return render(
        request,
        'cart.html',
        {'cart_items': cart_items, 'total_price': total_price, 'total_quantity': total_quantity}
    )


def delete_cart_item(request, pk):
    CartItem.objects.get(pk=pk).delete()
    return redirect('shop:cart')


def edit_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'decrement' and cart_item.quantity == 1:
        cart_item.delete()
        return redirect('shop:cart')
    if action == 'decrement' and cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('shop:cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:cart')


def location(request):
    return render(request, 'location.html')


# def create_order(request):
#     cart_items = CartItem.objects.filter(customer=request.user)
#     total_price = sum([item.total_price() for item in cart_items])
#     total_quantity = sum([item.quantity for item in cart_items])
#
#     form = OrderForm(request.POST)
#
#     if not cart_items:
#         return render(request, 'error.html')
#
#     if request.method == 'POST' and form.is_valid():
#         order = Order.objects.create(
#             customer=request.user,
#             address=request.POST.get('address'),
#             phone=request.POST.get('phone'),
#             total_price=total_price
#         )
#         for cart_item in cart_items:
#             OrderProduct.objects.create(
#                 order=order,
#                 product=cart_item.product,
#                 amount=cart_item.quantity,
#                 total=cart_item.total_price()
#             )
#         cart_items.delete()
#         return redirect('shop:orders')
#
#     return render(request, 'order.html', {
#         'cart_items': cart_items,
#         'total_price': total_price,
#         'total_quantity': total_quantity,
#         'form': form
#     })
#

# def orders(request):
#     orders_list = Order.objects.filter(customer=request.user)
#     return render(request, 'orders.html', {'orders': orders_list})


def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    return render(
        request,
        'cart.html',
        {'cart_items': cart_items, 'total_price': total_price, 'total_quantity': total_quantity}
    )


def delete_cart_item(request, pk):
    CartItem.objects.get(pk=pk).delete()
    return redirect('shop:cart')


def edit_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'decrement' and cart_item.quantity == 1:
        cart_item.delete()
        return redirect('shop:cart')
    if action == 'decrement' and cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('shop:cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:cart')


def create_order(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    form = OrderForm(request.POST)

    if not cart_items:
        return render(request, 'error.html')

    if request.method == 'POST' and form.is_valid():
        order = Order.objects.create(
            customer=request.user,
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            total_price=total_price
        )
        for cart_item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=cart_item.product,
                amount=cart_item.quantity,
                total=cart_item.total_price()
            )
        cart_items.delete()
        return redirect('shop:orders')

    return render(request, 'order.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity': total_quantity,
        'form': form
    })


def orders(request):
    orders_list = Order.objects.filter(customer=request.user)
    return render(request, 'orders.html', {'orders': orders_list})
