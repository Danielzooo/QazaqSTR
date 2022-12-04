from django.db import models


class FactorynameChoise(models.TextChoices):
    ALGA = 'alga', 'Алга'
    BIRKA = 'birka', 'Бирка'
    TERRA = 'terra', 'Терра'
    NO_NAME = 'no_name', 'Безымянный'
    