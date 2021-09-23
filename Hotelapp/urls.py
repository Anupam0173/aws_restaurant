from django.urls import path
from django.urls.conf import include
from Hotelapp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hview', views.HotelViewSet, basename='hotel')
# router.register('hpview', views.HotelProduct, basename='hotelproduct')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:id>/', views.particular_hotel_products)

    # path('pp/', views.ProductViewSet.as_view()),
]
