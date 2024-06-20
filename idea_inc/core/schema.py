from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializer import SkillSerializer

core_list_docs = extend_schema(
    responses=SkillSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Category of core items to retrieve",
        ),
        OpenApiParameter(
            name="qty",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Limit the number of core items returned",
        ),
        OpenApiParameter(
            name="by_user",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Filter core items by the current authenticated user",
        ),
        OpenApiParameter(
            name="by_coreid",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Filter core items by the specified core ID",
        ),
        OpenApiParameter(
            name="with_num_members",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Annotate each core item instance with the count of members associated with that core item",
        ),
    ],
)
