from django.contrib.auth import get_user_model
from django.http import Http404
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import mixins
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import json

User = get_user_model()


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer


class ShopList(generics.ListAPIView):
    queryset = Shop.objects.all().order_by("name")
    serializer_class = ShopListSerializer
    filter_backends = [
        filters.SearchFilter
    ]
    search_fields = [
        "name",
        "menu_items__name",
        "address__city",
        "address__province"
    ]


class ShopDetails(generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailsSerializer


class ShopDestroy(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner, IsShopOwnerOrReadOnly]
    queryset = Shop.objects.all()
    serializer_class = ShopDetailsSerializer


class ShopCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Shop.objects.all()
    serializer_class = ShopCreateUpdateSerializer


class ShopUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner, IsShopOwnerOrReadOnly]
    queryset = Shop.objects.all()
    serializer_class = ShopCreateUpdateSerializer


class ShopProfilePicture(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner, IsShopOwnerOrReadOnly]
    queryset = Shop.objects.all()
    serializer_class = ShopProfilePictureSerializer


class ShopOrderList(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner, IsShopOwnerOrReadOnly]
    serializer_class = ShopOrderListOrderSerializer
    lookup_url_kwarg = "shop_id"
    filter_backends = [
        filters.SearchFilter
    ]
    search_fields = [
        "=status"
    ]

    def get_queryset(self):
        shop_id = self.kwargs.get(self.lookup_url_kwarg)
        orders = Order.objects.filter(shop=shop_id).order_by("-created_at")

        return orders


class MenuItemCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsOwner, IsShopOwnerOrReadOnly]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemCreateSerializer


class MenuItemDestroy(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner, IsShopOwnerOrReadOnly]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemCreateSerializer


class MenuItemUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner, IsShopOwnerOrReadOnly]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemUpdateSerializer


class MenuItemPicture(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner, IsShopOwnerOrReadOnly]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemPictureSerializer


class OrderDetails(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderDetailsSerializer


class OrderCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderUpdateStatus(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderUpdateStatusSerializer


class UserProfile(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


class UserProfilePicture(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserProfilePictureSerializer


class UserMyShop(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, format=None):
        try:
            shop = Shop.objects.get(owner=request.user)
            serializer = UserMyShopSerializer(shop)
            return Response(serializer.data)

        except Shop.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserOrderList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserOrderListOrderSerializer
    lookup_url_kwarg = "user_id"
    filter_backends = [
        filters.SearchFilter
    ]
    search_fields = [
        "=status"
    ]

    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_url_kwarg)
        orders = Order.objects.filter(user=user_id).order_by("-created_at")

        return orders


class AuthUserDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = AuthUserSerializer(request.user)
        content = {
            "user": user.data,
        }

        return Response(content)


class AuthUserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class AuthUserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]


class AuthUserUpdatePassword(generics.UpdateAPIView):
    model = User
    serializer_class = UserPasswordSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
