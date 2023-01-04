from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
import csv
import random

# Create your views here.

def index(request):
    item = Item.objects.all()

    if len(item) == 0:
        items_csv = open("bibles/bible3.csv", encoding="UTF-8")
        items_reader = csv.reader(items_csv)
        bulk_list = []
        for i in items_reader:
            bulk_list.append(
                Item(
                    content=i[0],
                    content_en=i[1],
                    vers=i[2],
                    vers_en=i[3],
                    keyword=i[4],
                )
            )
        Item.objects.bulk_create(bulk_list)

    context = {
        "item": item,
        "love": love,
    }
    return render(request, "bibles/index.html")


def verse(request):
    items = list(Item.objects.all())
    verse_items = random.choice(items)
    # love = Item.objects.filter(keyword="사랑")
    # love_items = random.choice(love)
    context = {
        'verse_items' : verse_items,
        # 'love_items' : love_items,
    }
    return render(request, "bibles/verse.html", context)

def love(request):
    love = Item.objects.filter(keyword="사랑")
    love_items = random.choice(love)
    context = {
        'love_items' : love_items,
    }

    return render(request, "bibles/verse.html", context)


def wisdom(request):
    wisdom = Item.objects.filter(keyword="지혜")
    wisdom_items = random.choice(wisdom)
    context = {
        'wisdom_items' : wisdom_items,
    }

    return render(request, "bibles/verse.html", context)

def comfort(request):
    comfort = Item.objects.filter(keyword="위로")
    comfort_items = random.choice(comfort)
    context = {
        'comfort_items' : comfort_items,
    }

    return render(request, "bibles/verse.html", context)