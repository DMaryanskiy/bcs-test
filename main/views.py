from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Blockchain_blocks

def index(request):
    """
    View of the main page with list of all blocks ordered by
    ID decreased with pagination (100 items per page).
    """
    blocks = Blockchain_blocks.objects.all().order_by("-id")
    paginator = Paginator(blocks, 100)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(
        request,
        "index.html",
        {
            "page": page,
        }
    )

def block_detailed_view(request, height):
    """
    View of one single block using height parameter from url.
    """    
    block = get_object_or_404(Blockchain_blocks, height=height)

    context = {
        "height" : block.height,
        "hash" : block.hash,
        "timestamp" : block.timestamp,
        "miner" : block.miner,
        "transactionCount" : block.transactionCount,
    }

    return render(
        request,
        "block.html",
        context=context
    )
