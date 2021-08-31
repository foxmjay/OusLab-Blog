from django.shortcuts import render
from .models import Categorie
from django.contrib.auth.decorators import login_required
from .forms import CategorieForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
import re


@login_required
def categorie_list(request):
    categories = Categorie.objects.all()
    return render(request, 'backend/categories/list.html', {'categories': categories})


@login_required
def categorie_create(request):
    return render(request, 'backend/categories/create.html')


@login_required
def categorie_store(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.cleaned_data['name']
            categorie = form.save(commit=False)
            categorie.save()

            messages.error(request, "Info: Categories created successfully")
            return HttpResponseRedirect('/dashboard/categories')

        else:
            messages.error(request, "Error: Form not Valide")
    return render(request, 'backend/categories/create.html', {'form': form})


@login_required
def categorie_edit(request, categorie_id):
    categorie = get_object_or_404(Categorie, pk=categorie_id)
    return render(request, 'backend/categories/edit.html', {'categorie': categorie})


@login_required
def categorie_update(request, categorie_id):

    if request.method == 'POST':
        categorie = get_object_or_404(Categorie, pk=categorie_id)
        form = CategorieForm(request.POST, instance=categorie)
        # check whether it's valid:
        if form.is_valid():
            form.cleaned_data['name']
            categorie.save()
            messages.error(request, "Info: Categorie updated successfully")
            return HttpResponseRedirect('/dashboard/categories')

        else:
            messages.error(request, "Error: Form not Valide")

    return render(request, 'backend/categories/edit.html', {'form': form, 'categorie': categorie})


@login_required
def categorie_delete(request, categorie_id):
    categorie = get_object_or_404(Categorie, pk=categorie_id)
    categorie.delete()
    messages.error(request, "Info: Categorie deleted successfully")
    return HttpResponseRedirect('/dashboard/categories')
