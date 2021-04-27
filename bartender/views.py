from typing import ContextManager
from django.shortcuts import render
from django.views import View
from  django.http import HttpResponse


# The IndexView
class IndexView(View):
    def get(self,request):
        return render(request, 'bartender/index.html')
