# members/urls.py
from django.urls import path
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('new/', IndexView, name='new_member'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)