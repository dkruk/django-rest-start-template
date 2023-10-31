from django.db import models


class YesNoChoices(models.TextChoices):
    YES = "1", "Yes"
    NO = "0", "No"
