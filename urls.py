"""
urlconf for {{ project_name }} project.

For more information and examples, see 
https://docs.djangoproject.com/en/2.0/topics/http/urls/#example
"""

from django.conf import settings
from django.urls import include, re_path, path

from django.contrib import admin

urlpatterns = [
    # Examples:
    # path('', app.views.homepage, name='home'),
    # path('post/<int:id>/', app.views.view_post, name='view_post'),
    # re_path('articles/(?P<year>[0-9]{4})/', app.views.year_archive),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        urlpatterns.append(
            path('__debug__/', include('debug_toolbar.toolbar', namespace='djdt')),
        )

    # Serve media files in development. Note Django automatically serves
    # static files as the staticfiles app is active in settings.py.
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
