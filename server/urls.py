from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ProfileViewSet, ProjectViewSet, WorkViewSet, SkillViewSet, health
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"work", WorkViewSet)
router.register(r"skills", SkillViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("health", health),
    path("api-token-auth/", obtain_auth_token),  # auth endpoint
    path("", TemplateView.as_view(template_name="index.html")),
]
