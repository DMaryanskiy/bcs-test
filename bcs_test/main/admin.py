from django.contrib import admin
from .models import Blockchain_blocks

@admin.register(Blockchain_blocks)
class BlocksAdmin(admin.ModelAdmin):
    pass
