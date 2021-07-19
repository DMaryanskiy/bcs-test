import requests
from django.core.management.base import BaseCommand

from ...models import Blockchain_blocks

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        url = "https://bcschain.info/api/recent-blocks?count=500"
        response = requests.get(url)
        data = response.json()
        
        for block in data:
            block_data = Blockchain_blocks(
                height = block["height"],
                hash = block["hash"],
                timestamp = block["timestamp"],
                miner = block["miner"],
                transactionCount = block["transactionCount"],
            )
            block_data.save()