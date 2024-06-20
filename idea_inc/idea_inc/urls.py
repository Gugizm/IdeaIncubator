from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserCreateAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/create/", UserCreateAPIView.as_view(), name="user_create"),
    path("api/user/login/", obtain_auth_token, name="login"),
    path("api/user/account/", include("account.urls")),
    path("api/post/", include("post.urls")),
    path("api/comment/", include("comment.urls")),
    path("api/core/", include("core.urls")),
    path("api/notification/", include("notification.urls")),
    path("api/docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/ui/", SpectacularSwaggerView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
