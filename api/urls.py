from django.urls import path
from api.api import *

from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

urlpatterns = [

  path('antony/', admin.site.urls),
  path('v1/Get_menu', Get_menu.as_view(), name='Get_Menu'),
  path('v1/Get_menu_items/', Get_menu_items.as_view(), name='Get_menu_items'),
  path('v1/Get_menu_types/', Get_type_menu.as_view(), name='Get_menu_types')
]
