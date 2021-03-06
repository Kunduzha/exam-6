from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import Commentform
from webapp.models import Comments
# Create your views here.

def main_page(request):
    comment = Comments.objects.all()
    return render(request, "main.html", {'comment': comment})

def add_comment():
    pass

def dell_comment():
    pass

def update_comment():
    pass