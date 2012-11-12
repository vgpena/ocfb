from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.db import models
import datetime

from roster.models import Member
from events.models import Category, Event
from gallery.models import Gallery

def index(TemplateView):
	template_name = "index.html"
	
def roster(request):
	fullroster = Member.objects.order_by("weapon", "gender")

	return render_to_response("roster.html", {"roster": fullroster})
	
def events(request):
	categories = Category.objects.all()
	past_events = Event.objects.exclude(date__gte=datetime.datetime.now()).order_by("category")
	upcoming_events = Event.objects.filter(date__gte=datetime.datetime.now()).order_by("category")
	
	return render_to_response("events.html", {"categories": categories, "past": past_events, "upcoming": upcoming_events})
	
def gallery(request):
	galleries = Gallery.objects.order_by("index")
	
	return render_to_response("gallery.html", {"galleries": galleries})