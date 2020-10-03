from django.http import HttpResponseBadRequest
from rest_framework import serializers, pagination
from rest_framework.settings import api_settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from .models import *

User = get_user_model()

# Shop Related Seriailizers


class ShopListSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField()
    owner = serializers.StringRelatedField()
    address = serializers.StringRelatedField()

    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "owner",
            "contact_number",
            "profile_picture",
            "address"
        ]


class ShopDetailsMenuItemListSerializer (serializers.ModelSerializer):
    picture = serializers.ImageField()

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "price",
            "description",
            "picture"
        ]


class ShopDetailsSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField()
    owner = serializers.StringRelatedField()
    address = serializers.StringRelatedField()
    # menu_items = serializers.SerializerMethodField("paginated_menu_items")
    menu_items = ShopDetailsMenuItemListSerializer(many=True)

    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "owner",
            "profile_picture",
            "address",
            "contact_number",
            "menu_items"
        ]

    def paginated_menu_items(self, obj):
        menu_items = MenuItem.objects.filter(shop=obj)
        count = len(menu_items)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(menu_items, self.context["request"])
        serializer = ShopDetailsMenuItemListSerializer(
            page,
            many=True,
            context={"request": self.context["request"]}
        )
        data = {
            "count": count,
            "results": serializer.data
        }

        return data


class ShopAddressCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopAddress
        fields = [
            "line_1",
            "line_2",
            "barangay",
            "city",
            "province",
            "region",
            "zip_code"
        ]


class ShopCreateUpdateSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField(
        required=False, allow_empty_file=True)
    address = ShopAddressCreateUpdateSerializer()

    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "owner",
            "profile_picture",
            "contact_number",
            "address"
        ]

    # Django REST Framework does not support create for nested serializers by default
    def create(self, validated_data):
        address_data = validated_data.pop("address")
        shop = Shop(**validated_data)
        shop.save()
        shop_address = ShopAddress(shop=shop, **address_data)
        shop_address.save()

        return shop

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.contact_number = validated_data.get(
            "contact_number", instance.contact_number)
        instance.profile_picture = validated_data.get(
            "profile_picture", instance.profile_picture)
        updated_address = validated_data.get("address", instance.address)
        instance.address.line_1 = updated_address.get(
            "line_1", instance.address.line_1)
        instance.address.line_2 = updated_address.get(
            "line_2", instance.address.line_2)
        instance.address.barangay = updated_address.get(
            "barangay", instance.address.barangay)
        instance.address.city = updated_address.get(
            "city", instance.address.city)
        instance.address.province = updated_address.get(
            "province", instance.address.province)
        instance.address.region = updated_address.get(
            "region", instance.address.region)
        instance.address.zip_code = updated_address.get(
            "zip_code", instance.address.zip_code)
        instance.save()
        instance.address.save()

        return instance


class ShopProfilePictureSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField()

    class Meta:
        model = Shop
        fields = [
            "profile_picture"
        ]

    def update(self, instance, validated_data):
        instance.profile_picture = validated_data.get(
            "profile_picture", instance.profile_picture)
        instance.save()

        return instance


class MenuItemDetailsSerialzer(serializers.ModelSerializer):
    picture = serializers.ImageField()
    shop = serializers.StringRelatedField()

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "price",
            "description",
            "picture",
            "shop"
        ]


class MenuItemCreateSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False, allow_empty_file=True)
    shop = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "price",
            "description",
            "picture",
            "shop"
        ]


class MenuItemUpdateSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False, allow_empty_file=True)

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "price",
            "description",
            "picture",
        ]

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.description = validated_data.get(
            "description", instance.description)
        instance.picture = validated_data.get("picture", instance.picture)
        instance.save()

        return instance


class MenuItemPictureSerializer (serializers.ModelSerializer):
    picture = serializers.ImageField()

    class Meta:
        model = MenuItem
        fields = [
            "picture"
        ]

    def update(self, instance, validated_data):
        instance.picture = validated_data.get(
            "picture", instance.picture)
        instance.save()

        return instance


class OrderDetailsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    shop = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    menu_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "shop",
            "remark",
            "created_at",
            "status",
            "menu_items"
        ]

    def get_menu_items(self, obj):
        items = OrderMenuItem.objects.filter(order=obj.id)
        menu_items = []

        for item in items:
            menu_items.append({
                "name": item.menu_item.name,
                "quantity": item.quantity
            })

        return menu_items


class OrderCreateMenuItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all())

    class Meta:
        model = OrderMenuItem
        fields = [
            "menu_item",
            "quantity"
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    shop = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())
    items = OrderCreateMenuItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "shop",
            "remark",
            "items"
        ]

    def create(self, validated_data):
        menu_items = validated_data.pop("items")
        order = Order(**validated_data)
        order.save()

        for item in menu_items:
            # menu_item = MenuItem.objects.get(pk=item.menu_item)
            order_item = OrderMenuItem(
                menu_item=item.get("menu_item"),
                order=order,
                quantity=item.get("quantity")
            )

            order_item.save()

        return order


class OrderUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "status"
        ]

    def update(self, instance, validated_data):
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        return instance

# For retrieving user data used by nuxt $auth.user


class AuthUserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "type",
        ]


class UserProfileSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField()
    address = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "contact_number",
            "first_name",
            "last_name",
            "profile_picture",
            "address"
        ]


class UserAddressCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = [
            "line_1",
            "line_2",
            "barangay",
            "city",
            "province",
            "region",
            "zip_code"
        ]

# For creating new users


class UserCreateSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField(
        required=False, allow_empty_file=True)
    address = UserAddressCreateUpdateSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "contact_number",
            "first_name",
            "last_name",
            "profile_picture",
            "type",
            "address"
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        password = make_password(validated_data.pop("password"))
        user = User(password=password, **validated_data)
        user.save()
        user_address = UserAddress(user=user, **address_data)
        user_address.save()

        return user

# For updating user info


class UserUpdateSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField(
        required=False, allow_empty_file=True)
    address = UserAddressCreateUpdateSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "contact_number",
            "first_name",
            "last_name",
            "profile_picture",
            "address"
        ]

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.contact_number = validated_data.get(
            "contact_number", instance.contact_number)
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)
        instance.profile_picture = validated_data.get(
            "profile_picture", instance.profile_picture)
        updated_address = validated_data.get("address", instance.address)
        instance.address.line_1 = updated_address.get(
            "line_1", instance.address.line_1)
        instance.address.line_2 = updated_address.get(
            "line_2", instance.address.line_2)
        instance.address.barangay = updated_address.get(
            "barangay", instance.address.barangay)
        instance.address.city = updated_address.get(
            "city", instance.address.city)
        instance.address.province = updated_address.get(
            "province", instance.address.province)
        instance.address.region = updated_address.get(
            "region", instance.address.region)
        instance.address.zip_code = updated_address.get(
            "zip_code", instance.address.zip_code)
        instance.save()
        instance.address.save()

        return instance


# For updating user password


class UserPasswordSerializer (serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "old_password",
            "new_password"
        ]


class UserProfilePictureSerializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField()

    class Meta:
        model = User
        fields = [
            "profile_picture"
        ]

    def update(self, instance, validated_data):
        instance.profile_picture = validated_data.get(
            "profile_picture", instance.profile_picture)
        instance.save()

        return instance


class UserMyShopSerializer (serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = [
            "id"
        ]


class ShopOrderListOrderSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    user = serializers.SerializerMethodField()
    shop = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    menu_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "shop",
            "remark",
            "created_at",
            "status",
            "menu_items"
        ]

    def get_menu_items(self, obj):
        items = OrderMenuItem.objects.filter(order=obj.id)
        menu_items = []

        for item in items:
            menu_items.append({
                "name": item.menu_item.name,
                "price": item.menu_item.price,
                "quantity": item.quantity
            })

        return menu_items

    def get_user(self, obj):
        user = User.objects.get(pk=obj.user.id)
        request = self.context["request"]
        return {
            "id": user.id,
            "name": str(user),
            "address": str(user.address),
            "profile_picture": request.build_absolute_uri(user.profile_picture.url)
        }


class UserOrderListOrderSerializer(serializers.ModelSerializer):
    shop = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    menu_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id",
            "shop",
            "remark",
            "created_at",
            "status",
            "menu_items"
        ]

    def get_menu_items(self, obj):
        items = OrderMenuItem.objects.filter(order=obj.id)
        menu_items = []

        for item in items:
            menu_items.append({
                "name": item.menu_item.name,
                "price": item.menu_item.price,
                "quantity": item.quantity
            })

        return menu_items

    def get_shop(self, obj):
        shop = Shop.objects.get(pk=obj.shop.id)
        request = self.context["request"]
        return {
            "id": shop.id,
            "name": shop.name,
            "address": str(shop.address),
            "profile_picture": request.build_absolute_uri(shop.profile_picture.url)
        }
