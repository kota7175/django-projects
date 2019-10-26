from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = "homepages/index.html"
    
    
