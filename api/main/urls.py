from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("auth/user", views.AuthUserDetail.as_view()),
    path("auth/users", views.UserList.as_view()),
    path("auth/user/update/<int:pk>", views.AuthUserUpdate.as_view()),
    path("auth/user/change-password/<int:pk>",
         views.AuthUserUpdatePassword.as_view()),
    path("auth/register", views.AuthUserRegister.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
