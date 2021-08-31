from django.shortcuts import render
from .models import ViewLog
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
import re
from django.utils.crypto import get_random_string
from django.db.models import Count


@login_required
def viewlog_list(request):

    viewlogs = ViewLog.objects.all().order_by('-created_at')[:50]
    print("http://{}/".format(request.get_host()))
    counts = ViewLog.objects.all().values('url').annotate(total=Count('url')).order_by('total').filter(total__gt=10)
    return render(request, 'backend/viewlogs/list.html', {'viewlogs': viewlogs, 'viewCounts': counts})


@login_required
def viewlog_delete(request, viewlog_id):
    viewlog = get_object_or_404(ViewLog, pk=viewlog_id)
    viewlog.delete()
    messages.error(request, "Info: ViewLog deleted successfully")
    return HttpResponseRedirect('/dashboard/viewlogs')
