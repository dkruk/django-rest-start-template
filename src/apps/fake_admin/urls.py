from django.urls import path, re_path

from fake_admin.views import FakeAdminView

urlpatterns = [
    path('login/', FakeAdminView.as_view(), name='login'),
    re_path(r'^.*$', FakeAdminView.as_view(), name='index'),
]
