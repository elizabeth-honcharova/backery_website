from django.shortcuts import render, redirect
from .models import User, Item, Course, CartItem, Order, OrderItem
from django.db.models import Q
from .forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def home(request):
    items = Item.objects.all()[:8]
    context = {'items': items}
    return render(request, 'base/home.html', context)


def shop(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'base/shop.html', context)


def item(request, pk):
    item = Item.objects.get(id=pk)
    items = Item.objects.filter(
        Q(category__name__icontains=item.category)).exclude(Q(id=item.id))[:4]
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        cartItem, created = CartItem.objects.get_or_create(
            user=request.user, item=item,
            defaults={"quantity": 0},)
        cartItem.quantity += int(request.POST.get('quantity'))
        cartItem.save()
        return redirect('cart')
    context = {'item': item, 'items': items}
    return render(request, 'base/item_details.html', context)


def deleteCartItem(request, pk):
    item = CartItem.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('cart')
    return render(request, 'base/delete.html', {'obj': item})


def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'base/courses.html', context)


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price for item in cart_items)
    context = {'cart_items': cart_items, 'cart_total': total,
               'total': total + 55}
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        order = Order.objects.create(user=request.user,
                                     deliveryAddress=request.POST.get('deliveryAddress'), total_price=total)
        for cart_item in cart_items:
            OrderItem.objects.create(order=order,
                                     item=cart_item.item, quantity=cart_item.quantity)
            cart_item.delete()
        return redirect('orders')
    return render(request, 'base/cart.html', context)


def orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'base/orders.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    page = 'login'

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            return HttpResponse('User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is uncorrect')
    context = {'page': page}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page = 'register'
    form = MyUserCreationForm()
    context = {'page': page, 'form': form}
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('An error occurred during registration')

    return render(request, 'base/register.html', context)
