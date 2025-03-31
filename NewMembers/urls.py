from django.contrib import admin
from django.urls import path, include
from members.views import IndexView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView),
    path('members/', include('members.urls')),
]
