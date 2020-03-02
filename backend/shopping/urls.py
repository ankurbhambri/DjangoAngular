from django.urls import include, path
from rest_framework import routers

from shopping.views import ShoppingItemViewSet

router = routers.DefaultRouter()
router.register(
    'shopping-item', ShoppingItemViewSet, basename='shopping-item'
)

urlpatterns = [
    path('', include(router.urls)),
]