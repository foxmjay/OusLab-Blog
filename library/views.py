from django.shortcuts import render
from .models import Library
from django.contrib.auth.decorators import login_required
from .forms import LibraryForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
import re
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse
import json
import os


@login_required
def image_store(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            library = form.save(commit=False)
            library.name = library.path.name
            library.save()

            filename = os.path.basename(library.path.name)
            data_filename = "{}_{}".format(library.id, filename)

            return JsonResponse({"url": "/media/{}".format(library.path.name),
                                "data_filename": data_filename})

    return JsonResponse({"url": "/static/frontend/img/img-60x60.jpg",
                         "data_filename": "error"})


@login_required
def image_delete(request):
    if request.method == 'POST':
        # check whether it's valid:
        data_filename = request.POST.get('data_filename')

        if data_filename:
            data_filename = data_filename.split('_')
            library_id = data_filename[0]
            library_filename = data_filename[1]
            library = Library.objects.filter(id=library_id,
                                             path__contains=library_filename).first()
            library.delete()
            return JsonResponse({"ok": "ok"})
    return JsonResponse({"ok": "ok"})
