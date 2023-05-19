from django.contrib import admin
from .models import User, Item, Category, Course, Order, CartItem, OrderItem

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
