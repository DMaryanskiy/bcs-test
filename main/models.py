from django.db import models
from unixtimestampfield.fields import UnixTimeStampField

class Blockchain_blocks(models.Model):
    height = models.PositiveIntegerField(null=True)
    hash = models.CharField(max_length=64, null=True)
    timestamp = UnixTimeStampField(default=0.0)
    miner = models.CharField(max_length=80, null=True)
    transactionCount = models.PositiveIntegerField(null=True)  
