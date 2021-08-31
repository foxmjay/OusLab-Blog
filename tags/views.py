from django.shortcuts import render
from .models import Tag
from django.contrib.auth.decorators import login_required
from .forms import TagForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
import re


@login_required
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'backend/tags/list.html', {'tags': tags})


@login_required
def tag_create(request):
    return render(request, 'backend/tags/create.html')


@login_required
def tag_store(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.cleaned_data['name']
            tag = form.save(commit=False)
            tag.save()

            messages.error(request, "Info: Tag created successfully")
            return HttpResponseRedirect('/dashboard/tags')

        else:
            messages.error(request, "Error: Form not Valide")

    return render(request, 'backend/tags/create.html', {'form': form})


@login_required
def tag_edit(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'backend/tags/edit.html', {'tag': tag})


@login_required
def tag_update(request, tag_id):
    if request.method == 'POST':

        tag = get_object_or_404(Tag, pk=tag_id)
        form = TagForm(request.POST, instance=tag)

        # check whether it's valid:
        if form.is_valid():

            form.cleaned_data['name']
            tag.save()

            messages.error(request, "Info: Tag updated successfully")
            return HttpResponseRedirect('/dashboard/tags')

        else:
            messages.error(request, "Error: Form not Valide")

    return render(request, 'backend/tags/edit.html', {'form': form,
                                                      'tag': tag})


@login_required
def tag_delete(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    tag.delete()
    messages.error(request, "Info: Tag deleted successfully")
    return HttpResponseRedirect('/dashboard/tags')
