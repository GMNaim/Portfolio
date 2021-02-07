from django.urls import path, include
from rest_framework import routers

from my_portfolio.api.v1.viewsets import (CategoryViewSet,
                                          ImageViewSet,
                                          TechnologyViewSet,
                                          ProjectViewSet)

router = routers.DefaultRouter()
router.register('project-category', CategoryViewSet)
router.register('project-image', ImageViewSet)
router.register('project-technology', TechnologyViewSet)
router.register('project', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
