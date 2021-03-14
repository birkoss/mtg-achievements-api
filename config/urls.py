from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

urlpatterns = [
    #path('logout/', admin.site.urls, name='logout'),

    path('admin/', admin.site.urls),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
