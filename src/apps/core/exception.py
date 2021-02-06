from typing import Optional

from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _


class ServiceException(Exception):
    default_detail = _('Service Exception')

    def __init__(self, detail: Optional[str] = None) -> None:
        if detail is None:
            detail = self.default_detail

        self.detail = force_str(detail)

    def __str__(self) -> str:
        return self.detail
