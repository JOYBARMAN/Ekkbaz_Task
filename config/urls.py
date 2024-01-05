from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    # user urls
    path("api/v1/users", include("core.rest.urls.base")),
    # authentication urls
    path("api/v1/auth/", include("authentication.rest.urls.authentications")),
    # business urls
    path("api/v1/business", include("business.rest.urls.business")),
    # silk url
    path("silk/", include("silk.urls", namespace="silk")),
    # Spectacular url
    path("", SpectacularSwaggerView.as_view(), name="api-docs"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
