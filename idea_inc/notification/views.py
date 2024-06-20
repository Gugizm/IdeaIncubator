from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Notification
from .schema import notification_list_docs
from .serializer import NotificationSerializer


@notification_list_docs
class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(recipient=self.request.user).order_by("-timestamp")
