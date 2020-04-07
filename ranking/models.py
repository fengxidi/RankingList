from django.db import models

# Create your models here.


class RankModel(models.Model):

    account = models.CharField(max_length=30)
    score = models.IntegerField()
    rank = models.IntegerField(null=True)
