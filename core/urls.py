from rest_framework import routers
from django.urls import path, include
from core.views import *

router = routers.SimpleRouter()

router.register(r'company', CompanyViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'offer', OfferViewSet)
router.register(r'product', ProductViewSet)

core_patterns = ([
    path('', include(router.urls)),
])
