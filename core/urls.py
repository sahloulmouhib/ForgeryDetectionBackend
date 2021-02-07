from django.contrib import admin
from django.urls import path
# task2.views import ReviewEmailView
from task2.views import client_view,home_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/',client_view, name="reviews"),
   path('',home_view, name="home"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)