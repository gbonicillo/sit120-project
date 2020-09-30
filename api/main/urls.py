from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = []

auth_url_patterns = [
    path("auth/user", views.AuthUserDetails.as_view()),
    path("auth/users", views.UserList.as_view()),
    path("auth/users/<int:pk>", views.UserProfile.as_view()),
    path("auth/users/<int:pk>/update", views.AuthUserUpdate.as_view()),
    path("auth/users/<int:pk>/change-password",
         views.AuthUserUpdatePassword.as_view()),
    path("auth/register", views.AuthUserRegister.as_view()),
]

shop_url_patterns = [
    path("shops/", views.ShopList.as_view()),
    path("shops/create", views.ShopCreate.as_view()),
    path("shops/<int:pk>", views.ShopDetails.as_view()),
    path("shops/<int:pk>/update", views.ShopUpdate.as_view()),
    path("shops/<int:pk>/destroy", views.ShopDestroy.as_view())
]

menu_item_url_patterns = [
    path("menu-items/create", views.MenuItemCreate.as_view()),
    path("menu-items/<int:pk>/destroy", views.MenuItemDestroy.as_view()),
    path("menu-items/<int:pk>/update", views.MenuItemUpdate.as_view())
]

order_item_url_patterns = [
    path("orders/create", views.OrderCreate.as_view()),
    path("orders/<int:pk>", views.OrderDetails.as_view()),
    path("orders/<int:pk>/update-status", views.OrderUpdateStatus.as_view())
]

urlpatterns += auth_url_patterns
urlpatterns += shop_url_patterns
urlpatterns += menu_item_url_patterns
urlpatterns += order_item_url_patterns

urlpatterns = format_suffix_patterns(urlpatterns)
