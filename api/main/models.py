from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from .extras.base_models import AbstractAddress

# User Model
# Extends Django's default User Model

fs_storage = FileSystemStorage()


class User(AbstractUser):

    CUSTOMER = "CS"
    OWNER = "OW"

    USER_TYPE_CHOICES = [
        (CUSTOMER, "customer"),
        (OWNER, "owner")
    ]

    email = models.EmailField(unique=True, null=False)
    contact_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(
        upload_to="users",
        default="/defaults/user.png",
        storage=fs_storage,
        blank=True
    )
    type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default=CUSTOMER
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Shop Model


class Shop(models.Model):

    name = models.CharField(unique=True, null=False, max_length=60)
    owner = models.OneToOneField(
        get_user_model(),  # In case we change our User model to something else
        related_name="shop",
        on_delete=models.CASCADE
    )
    contact_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(
        upload_to="shops/",
        default="/defaults/user.png",
        storage=fs_storage,
        blank=True
    )

    def __str__(self):
        return self.name

# User Address Model


class UserAddress(AbstractAddress):

    user = models.OneToOneField(
        get_user_model(),  # In case we change our User model to something else
        related_name="address",
        on_delete=models.CASCADE
    )

# Shop Address Model


class ShopAddress(AbstractAddress):

    shop = models.OneToOneField(
        Shop,
        related_name="address",
        on_delete=models.CASCADE
    )

# Menu Item Model


class MenuItem(models.Model):

    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False
    )
    description = models.TextField(default="No description given...")
    picture = models.ImageField(
        upload_to="menu-items/",
        default="/defaults/generic.png",
        storage=fs_storage,
        blank=True
    )

    shop = models.ForeignKey(
        Shop,
        related_name="menu_items",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

# Order Model


class Order(models.Model):
    PENDING = "PD"
    ACCEPTED = "AC"
    REJECTED = "RJ"
    CANCELED = "CN"

    ORDER_STATUS_CHOICES = [
        (PENDING, "pending"),
        (ACCEPTED, "accepted"),
        (REJECTED, "rejected"),
        (CANCELED, "canceled")
    ]

    user = models.ForeignKey(
        get_user_model(),  # In case we change our User model to something else
        related_name="orders",
        on_delete=models.CASCADE
    )
    shop = models.ForeignKey(
        Shop,
        related_name="orders",
        on_delete=models.CASCADE
    )
    remark = models.TextField(default="No remarks")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS_CHOICES,
        default=PENDING
    )

    menu_items = models.ManyToManyField(MenuItem, through="OrderMenuItem")

    def __str__(self):
        return f"order_{self.id}_{self.created_at}"

# Intermediate Model for Order and MenuItems


class OrderMenuItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField()
