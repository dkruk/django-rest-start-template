"""Project URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_v1_urlpatterns: list = [
    # API documentation
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(url_name='api_v1:schema'),
        name='schema-swagger-ui',
    )

]

urlpatterns = [
    path('admin/', include(('fake_admin.urls', 'fake_admin'), namespace='fake_admin')),

    path('api/v1/', include((api_v1_urlpatterns, 'api_v1'))),
    path(f'{settings.DJANGO_ADMIN_URL}/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
