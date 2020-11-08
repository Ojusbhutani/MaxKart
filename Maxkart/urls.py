from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('card', views.card),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)