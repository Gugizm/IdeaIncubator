from django.urls import include, path

from .views import NotificationListView

urlpatterns = [
    path("", NotificationListView.as_view(), name="notification-list"),
]
