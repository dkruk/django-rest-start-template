from typing import TYPE_CHECKING

from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from authentication.models import AuthToken
from core.choices import YesNoChoices

if TYPE_CHECKING:
    from django.db.models.query import QuerySet


class ExpiredTokenFilter(admin.SimpleListFilter):

    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title: str = _('Expired')

    # Parameter for the filter that will be used in the URL query.
    parameter_name: str = 'expired'

    def lookups(self, *_args) -> list[tuple[str, str]]:
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return YesNoChoices.choices

    def queryset(
        self,
        _request: 'AuthToken',
        queryset: 'QuerySet[AuthToken]',
    ) -> 'QuerySet[AuthToken]':
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """

        now = timezone.now()
        value = self.value()

        if value is None:
            return queryset.all()
        elif value == YesNoChoices.YES.value:
            return queryset.filter(expires_at__lte=now)
        elif value == YesNoChoices.NO.value:
            return queryset.filter(expires_at__gt=now)


class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created_at', 'expires_at', 'user_agent')
    list_filter = (ExpiredTokenFilter, )
    list_select_related = ('user', )
    search_fields = ('user__first_name', 'user__last_name', 'user__email')


admin.site.register(AuthToken, AuthTokenAdmin)
