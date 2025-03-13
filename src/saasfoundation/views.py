import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *args, **kwargs):
  total_visits = PageVisit.objects.all()
  current_page_visits = PageVisit.objects.filter(path=request.path)

  context = {
    "page_title": "My Page",
    "page_body": "My Body",
    "current_page_visits": current_page_visits.count(),
    "total_visits": total_visits.count(),
  }

  PageVisit.objects.create(path=request.path)
  html_template = "home.html"
  return render(request, html_template, context)

def about_view(request, *args, **kwargs):
  return home_view(request, *args, **kwargs)