from django.db import models

class Blockchain_blocks(models.Model):
    height = models.PositiveIntegerField(null=True)
    hash = models.CharField(max_length=64, null=True)
    timestamp = models.CharField(null=True)
    miner = models.CharField(max_length=80, null=True)
    transactionCount = models.PositiveIntegerField(null=True)  
