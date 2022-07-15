from statistics import mode
from django.conf import settings
from django.db import models

from ..models import Meal


class MealPlan(models.Model):
    """Daily Meal Plan"""
    date = models.DateField()
    # check if needs cascade deleting
    meals = models.ManyToManyField(Meal, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.date
