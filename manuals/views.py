from django.shortcuts import render

from django.views.generic import ListView,DetailView
from .models import Manual


class ManualListView(ListView):
    model = Manual
    template_name = "manuals/manual_list.html"
    context_object_name = "manuals"

class ManualDetailView(DetailView):
    model = Manual
    template_name = "manuals/manual_detail.html"
    context_object_name = "manual"

# Create your views here.
