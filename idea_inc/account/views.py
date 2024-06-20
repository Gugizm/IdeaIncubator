from rest_framework import permissions, viewsets

from .models import AccountUser
from .schema import account_list_docs
from .serializer import AccountSerializer


# TODO define with viewsets
@account_list_docs
class AccountModelViewSet(viewsets.ModelViewSet):
    queryset = AccountUser.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
