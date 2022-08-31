from app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



app_name='app'

urlpatterns = [
	
    path('', views.home, name='home'),
    path('bar-generate/', views.generate_bar_view, name='generate-bar-view'),
    path('bar-generated/', views.generated_bar_view, name='generated-bar-view'),
    path('qr-generate/', views.generate_qr_view, name='generate-qr-view'),
    path('qr-generated/', views.generated_qr_view, name='generated-qr-view'),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
