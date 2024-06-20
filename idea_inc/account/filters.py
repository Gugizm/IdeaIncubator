import django_filters

from .models import AccountUser


class AccountFilter(django_filters.FilterSet):

    class Meta:
        model = AccountUser
        fields = ["id", "owner"]
