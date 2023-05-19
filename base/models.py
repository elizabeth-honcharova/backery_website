from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.TextField(null=True, blank=True,
                               default="A moist, flavorful, cake with golden raisins, shredded carrots, This cake is filled with a cream cheese filling. We also use this same recipe for our morning glory that has a honey glaze on top instead of the frosting, great for breakfast.")
    imagePath = models.CharField(max_length=200, default="f1.jpg")

    def __str__(self) -> str:
        return str(self.name)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def total_price(self):
        return self.quantity * self.item.price

    total_price = property(total_price)


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="user")
    deliveryAddress = models.CharField(max_length=200, null=True)
    total_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    def order_items(self):
        order_items = OrderItem.objects.filter(order=self)
        return ', '.join(str(item.item.name) for item in order_items)
    order_items = property(order_items)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def total_price(self):
        return self.quantity * self.item.price

    total_price = property(total_price)

    def __str__(self) -> str:
        return str(self.item.name)


class Course(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    imagePath = models.CharField(max_length=200, default="b1.jpg")

    def __str__(self) -> str:
        return str(self.name)
