from django.core.cache.backends.dummy import DummyCache


class ExtendedDummyCache(DummyCache):
    def keys(self, *args: tuple, **kwargs: dict) -> list:
        return list()
