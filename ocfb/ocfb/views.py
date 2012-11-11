from django.shortcuts import render_to_response
from django.views.generic import TemplateView

from roster.models import Member

def index(TemplateView):
	template_name = "index.html"
	
def roster(request):
	fullroster = Member.objects.all()

	return render_to_response("roster.html", {"roster": fullroster})