from django.db import models


class Leaderboard(models.Model):
    user = models.CharField(max_length=200)
    score = models.IntegerField()

    def __str__(self):
        text = self.user + " " + str(self.score)
        return text
