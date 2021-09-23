from django.urls import path
from django.urls.conf import include
from Productapp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pview', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    # path('pp/', views.ProductViewSet.as_view()),
]
