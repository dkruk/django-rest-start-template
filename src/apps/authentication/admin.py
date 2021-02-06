from typing import Final

from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from authentication.models import AuthToken


class ExpiredTokenFilter(admin.SimpleListFilter):
    YES: Final = '1'
    NO: Final = '0'

    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Expired')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'expired'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            (self.YES, _('Yes')),
            (self.NO, _('No')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """

        now = timezone.now()
        value = self.value()

        if value is None:
            return queryset.all()
        elif value == self.YES:
            return queryset.filter(expires_at__lte=now)
        elif value == self.NO:
            return queryset.filter(expires_at__gt=now)


class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created_at', 'expires_at', 'user_agent')
    list_filter = (ExpiredTokenFilter, )
    list_select_related = ('user', )
    search_fields = ('user__first_name', 'user__last_name', 'user__email')


admin.site.register(AuthToken, AuthTokenAdmin)
