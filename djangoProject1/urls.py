"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api_pizzeria.views.pizza_view import PizzaListApi, PizzaCreateApi, PizzaDetailApi, PizzaUpdateApi, PizzaDeleteApi
from api_pizzeria.views.pizzeria_view import PizzeriaListApi, PizzeriaCreateApi, PizzeriaDetailApi, PizzeriaUpdateApi, \
    PizzeriaDeleteApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza/', include(
        [
            path('', PizzaListApi.as_view(), name='list'),
            path('create/', PizzaCreateApi.as_view(), name='create'),
            path('detail/<int:pk>/', PizzaDetailApi.as_view(), name='detail'),
            path('update/<int:pk>/', PizzaUpdateApi.as_view(), name='update'),
            path('delete/<int:pk>/', PizzaDeleteApi.as_view(), name='delete'),
        ]
    )),

    path('pizzeria/', include(
        [
            path('', PizzeriaListApi.as_view(), name='list'),
            path('create/', PizzeriaCreateApi.as_view(), name='create'),
            path('detail/<int:pk>/', PizzeriaDetailApi.as_view(), name='detail'),
            path('update/<int:pk>/', PizzeriaUpdateApi.as_view(), name='update'),
            path('delete/<int:pk>/', PizzeriaDeleteApi.as_view(), name='delete'),
        ]
    ))

]
