"""smartparking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from account.api.viewsets import UserViewSet, RegisterUserViewSet, LogoutUserViewSet
from core.api.viewsets import StatusViewSet
from driver.api.viewsets import DriverViewSet, VehicleViewSet
from parking.api.viewsets import ParkingViewSet, ParkingSpotViewSet
from booking.api.viewsets import BookingViewSet


router = routers.DefaultRouter()

# App: Accounts - Contas
router.register('user', UserViewSet, basename='user')
router.register('register', RegisterUserViewSet, basename='register')
# router.register('update-user', UpdateUserViewSet, basename='update-user')
router.register('logout', LogoutUserViewSet, basename='logout')
# App: Core - Gerais
router.register('status', StatusViewSet, basename='status')
# router.register('states', StateViewSet, basename='states')
# router.register('cities', CityViewSet, basename='cities')
# App: Driver - Motoristas
router.register('drivers', DriverViewSet, basename='drivers')
router.register('vehicles', VehicleViewSet, basename='vehicles')
# App: Driver - Estacionamentos
router.register('parkings', ParkingViewSet, basename='parkings')
router.register('parking-spots', ParkingSpotViewSet, basename='parking-spots')
# App: Booking - Livro de Registros
router.register('bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('', include(router.urls)),
    path('login/parking/', obtain_auth_token),
    path('login/driver/', obtain_auth_token),
    path('admin/', admin.site.urls),
]
