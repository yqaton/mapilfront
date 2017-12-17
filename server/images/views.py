import sys
from django.shortcuts import render
from PIL import Image, ImageFilter

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def handle_image(request):
    try:
        im = Image.open(request)
        im = im.filter(ImageFilter.CONTOUR)
        response = HttpResponse(content_type="image/jpeg")
        im.save(response, "JPEG")
        return response
    except IOError:
        red = Image.new('RGB', (50, 50), (255,0,0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response
