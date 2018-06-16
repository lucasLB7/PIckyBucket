from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image,Category,Tag, Location, NewsLetterRecipients
from django.db.models import Q
from .forms import NewsLetterForm


'''
We create the xmain view for our home page:
    - View "featured" pictures
    - View picture poster
    - View picture date
'''

def home_main(request):
    view_images = Media.display_all_media()
    display_categories = Category.objects.all()
    display_tags = Tag.objects.all()