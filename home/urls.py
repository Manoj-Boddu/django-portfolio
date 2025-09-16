from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('internalHome.urls')),
    # If you have blog views, include them like this:
    # path('blog/', include('blog.urls')),
]

# Serve media files in development and Render
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
