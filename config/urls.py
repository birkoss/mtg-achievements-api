from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

from users.api.urls import urlpatterns as users_urlpatterns

urlpatterns = [
    #path('logout/', admin.site.urls, name='logout'),

    path('admin/', admin.site.urls),

] + users_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)