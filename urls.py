from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^another_app/', include('another_app.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns.append(
            url(r'^__debug__/', include(debug_toolbar.urls)),
        )

    # Serve media files in development. Note Django automatically serves
    # static files as the staticfiles app is active in settings.py.
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
