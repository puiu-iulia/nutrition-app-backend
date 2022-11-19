from email.policy import default
from statistics import mode
from django.conf import settings
from enum import unique
from django.db import models
import datetime

from ..models import Meal


class MealPlan(models.Model):
    """Daily Meal Plan"""
    meal_date = models.DateField(
        unique=True, blank=False, default=datetime.datetime.now())
    date = models.DateField()
    # check if needs cascade deleting
    meals = models.ManyToManyField(Meal, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.date
