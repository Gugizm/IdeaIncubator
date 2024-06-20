from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializer import CommentSerializer

comment_list_docs = extend_schema(
    responses=CommentSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="post",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Filter comments by post ID",
        ),
        OpenApiParameter(
            name="user",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Filter comments by user ID",
        ),
    ],
)
