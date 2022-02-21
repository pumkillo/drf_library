from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from .views import *

# app_name = 'main'

router = DefaultRouter()
router.register(r'books', AllBooksViewSet)
router.register(r'authors', AuthorViewSet)
# router.register('search/', SearchView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

