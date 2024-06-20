from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializer import UserCreateSerializer

user_list_docs = extend_schema(
    responses=UserCreateSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="username",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Filter users by username",
        ),
        OpenApiParameter(
            name="password",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Create password",
        ),
        OpenApiParameter(
            name="email",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Filter users by email",
        ),
        OpenApiParameter(
            name="is_active",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Filter users by active status",
        ),
        OpenApiParameter(
            name="date_joined",
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY,
            description="Filter users by the date they joined",
        ),
    ],
)
