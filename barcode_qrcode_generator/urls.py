from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gen-admin/', admin.site.urls),
    path('', include('app.urls', namespace='app'))
]