from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializer import NotificationSerializer

notification_list_docs = extend_schema(
    responses=NotificationSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Category of notifications to retrieve",
        ),
        OpenApiParameter(
            name="qty",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Limit the number of notifications returned",
        ),
        OpenApiParameter(
            name="by_user",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Filter notifications by the current authenticated user",
        ),
        OpenApiParameter(
            name="by_notificationid",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Filter notifications by the specified notification ID",
        ),
        OpenApiParameter(
            name="with_num_members",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Annotate each notification instance with the count of members associated with that notification",
        ),
    ],
)
