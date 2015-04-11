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
from datetime import datetime, timedelta

# Create your views here.
def home(request):
	msg = None
	if request.method == 'POST':
		ticker = request.POST.get('ticker', None)
		if ticker:
			return HttpResponseRedirect("result?ticker=%s"%ticker)
		else:
			msg = "Oh snap! You haven't type anything."

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

	if not stock.get_open():
		msg = "Sorry. The company you are trying to find is not existed."

	start = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
	end = datetime.now().strftime('%Y-%m-%d')
	historical = stock.get_historical(start, end)

	context = {
		"msg": msg,
		"ticker": ticker,
		"stock": stock,
		"historical": unicode(historical)
	}
	return render(request, "result.html", context)