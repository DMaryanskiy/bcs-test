from django.urls import path
from .views import index, block_detailed_view


urlpatterns = [
    path("", index),
    path("blocks/<int:height>", block_detailed_view),
]