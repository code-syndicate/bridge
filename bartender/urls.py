from django.urls import path
from django.urls import path
from .import views

urlpatterns  = [
    path('', views.IndexView.as_view(), name =  'indexview'),
    path('token/', views.TokenView.as_view(), name = 'tokenview')
]
