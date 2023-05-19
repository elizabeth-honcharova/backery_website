from django.forms import ModelForm
from .models import CartItem, User, Order
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CartItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = '__all__'
