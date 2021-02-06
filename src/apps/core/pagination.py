from rest_framework.pagination import LimitOffsetPagination


class LimitedOffsetPagination(LimitOffsetPagination):
    max_limit = 100
