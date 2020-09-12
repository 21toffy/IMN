
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletters/', include('newsletters.urls', namespace='newsletters')),
    path('control/', include('controlpanel.urls', namespace='controlpanel')),
    path('course/', include('courses.urls', namespace='courses')),
    path('', include('myapp.urls', namespace='myapp')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

