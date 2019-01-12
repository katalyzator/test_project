from django.shortcuts import render

from main.models import Item


def index_view(request):
    items = Item.objects.all()

    context = {"items": items}
    template = 'index.html'

    return render(request, template, context)


def item_detail_view(request, pk):
    item = Item.objects.get(pk=pk)

    context = {"item": item}
    template = 'item_detail.html'

    return render(request, template, context)
