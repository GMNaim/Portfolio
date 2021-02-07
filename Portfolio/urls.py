from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_portfolio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_url=settings.STATIC_ROOT, show_indexes=True)
    urlpatterns += static(settings.MEDIA_URL, document_url=settings.MEDIA_ROOT, show_indexes=True)
