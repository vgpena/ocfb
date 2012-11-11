from django.shortcuts import render_to_response
from django.views.generic import TemplateView

from roster.models import Member
from events.models import Category, Event

def index(TemplateView):
	template_name = "index.html"
	
def roster(request):
	fullroster = Member.objects.all()

	return render_to_response("roster.html", {"roster": fullroster})
	
def events(request):
	categories = Category.objects.all()
	events = Event.objects.order_by('date')
	
	return render_to_response("events.html", {"categories": categories, "events": events})