from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *
# Create your views here.

class Get_menu_items(APIView):
    def get(self,request):
        token = request.Get.get('token')
        arg  = request.GET.get("menu")
        type = request.GET.get("type")
        menuItems = MenuItem.objects.filter(menu = arg,type = type )
        menuItems_ser = MenuItemSerializer(menuItems, many=True)
        return Response(menuItems_ser.data)

class Get_menu(APIView):
    def get(self):
        season = []
        menus = Menu.objects.all()
        for x in menus:
            if x.isActive == True:
                season += x
        season_ser = MenuSerializer(season, many=True)
        return Response(season_ser.data)
class Get_type_menu(APIView):
    def get(self,request):
        arg = request.GET.get("season")
        types = Type.objects.filter(season = arg)

        sorted(types, key=lambda queue: queue.queue_view)
        type_ser = TypeSerializer(types, many=True)
        return Response(type_ser.data)

