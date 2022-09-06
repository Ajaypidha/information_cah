from django import views
from django.shortcuts import render
from requests import request
from django.views import View

from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(30)
class storage_view(View):
    def get(self,request):
         return render(request,'cacheapp/storage.html')

class home_view(View):
    def get(self,request):
        return render(request,'cacheapp/storage.html')






