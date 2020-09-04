
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

import myapp.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletters/', include('newsletters.urls', namespace='newsletters')),
    path('', include('myapp.urls', namespace='myapp')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

