from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('', include('library.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='library/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tinymce/', include('tinymce.urls')),
] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

handler404 = 'library.views.page_not_found_view'
handler500 = 'django.views.defaults.server_error'
handler403 = 'library.views.permission_denied_view'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)