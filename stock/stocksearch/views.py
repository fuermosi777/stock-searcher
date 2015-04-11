from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
import datetime
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.template import Context
from operator import __or__ as OR
from yahoo_finance import Share

# Create your views here.
def home(request):
	if request.method == 'POST':
		ticker = request.POST.get('ticker', None)
		if ticker:
			return HttpResponseRedirect("result?ticker=%s"%ticker)
		else:
			pass

	context = {}
	return render(request, "home.html", context)

def result(request):
	context = {}
	return render(request, "result.html", context)