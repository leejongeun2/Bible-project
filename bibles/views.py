from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
import csv

# Create your views here.

def index(request):
    return render(request, "bibles/index.html")
    # item = Item.objects.all()

    # if len(item) == 0:
    #     items_csv = open("products/shopping3.csv", encoding="UTF-8")
    #     items_reader = csv.reader(items_csv)
    #     bulk_list = []
    #     for i in items_reader:
    #         bulk_list.append(
    #             Item(
    #                 title=i[0],
    #                 price=i[1],
    #                 image_url=i[2],
    #             )
    #         )
    #     Item.objects.bulk_create(bulk_list)
    # # pagination
    # ordered_item = Item.objects.order_by("pk")
    # paginator = Paginator(ordered_item, 9)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # context = {
    #     "item": item,
    #     "page_obj": page_obj,
    # }
    # return render(request, "products/index.html", context)