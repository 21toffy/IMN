
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

import myapp.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls', namespace='myapp')),
    # path('blog/', include('blog.urls', namespace='blog')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

