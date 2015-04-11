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
	msg = None
	if request.method == 'POST':
		ticker = request.POST.get('ticker', None)
		if ticker:
			return HttpResponseRedirect("result?ticker=%s"%ticker)
		else:
			msg = "Oh snap! You haven't type anything!"

	context = {
		"msg": msg
	}
	return render(request, "home.html", context)

def result(request):
	msg = None
	try:
		ticker = request.GET.get('ticker', None)
	except:
		raise Http404

	stock = Share(ticker)

	context = {
		"msg": msg,
		"open": stock.get_open()
	}
	return render(request, "result.html", context)