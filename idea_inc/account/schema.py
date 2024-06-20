from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializer import AccountSerializer

account_list_docs = extend_schema(
    responses=AccountSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="status",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Filter accounts by status",
        ),
        OpenApiParameter(
            name="role",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Filter accounts by role",
        ),
        OpenApiParameter(
            name="created_after",
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY,
            description="Filter accounts created after a specific date",
        ),
    ],
)
