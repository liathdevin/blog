from django.db import models
from django.contrib.auth.models import User


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default="0")

    def __str__(self):
        text = str(self.user) + " " + str(self.score)
        return text
