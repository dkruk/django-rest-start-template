from typing import Any

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import generic

from fake_admin.forms import FakeAdminLoginForm


class FakeAdminView(generic.FormView):
    template_name = "fake_admin/login.html"
    form_class = FakeAdminLoginForm

    def dispatch(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: dict,
    ) -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponse:
        if not request.path.endswith("/"):
            return redirect(request.path + "/", permanent=True)

        # Django redirects the user to an explicit login view with
        # a next parameter, so emulate that.
        login_url = reverse("fake_admin:login")
        if request.path != login_url:
            return redirect_to_login(request.get_full_path(), login_url)

        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class: type[FakeAdminLoginForm] = form_class) -> FakeAdminLoginForm:
        return form_class(self.request, **self.get_form_kwargs())

    def get_context_data(self, **kwargs: dict) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        path = self.request.get_full_path()
        context.update(
            {
                "app_path": path,
                REDIRECT_FIELD_NAME: reverse("fake_admin:index"),
                "title": _("Log in"),
            }
        )
        return context

    def form_valid(self, form: FakeAdminLoginForm) -> HttpResponse:
        return self.form_invalid(form)
