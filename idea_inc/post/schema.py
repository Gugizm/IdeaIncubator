from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializer import PostSerializer

post_list_docs = extend_schema(
    responses=PostSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="author",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Filter posts by author ID",
        ),
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Filter posts by category",
        ),
        OpenApiParameter(
            name="published",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Filter posts by published status",
        ),
        OpenApiParameter(
            name="tags",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Filter posts by tags (comma-separated)",
        ),
    ],
)
