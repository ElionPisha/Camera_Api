from django.shortcuts import render
from .models import Camera
from django.http import HttpResponse


def index(request):
    all_Data = Camera.objects.all()
    return render(request, "index.html", {'data' : all_Data})



# URL = "https://standalone.kupferschluessel.de/content.php?werkstoff=01672&werkstoff2=06634&lang=german&sortgruppe=7808"
#
#
#
# def index(request):
#     r = requests.get(URL)
#     print(r.content)
#     context = {'tem': r.content}
#     return render(request, "index.html", context)