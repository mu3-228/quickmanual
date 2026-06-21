from django.shortcuts import render

from django.views.generic import ListView,DetailView
from django.db.models import Q
from .models import Manual


class ManualListView(ListView):
    model = Manual
    template_name = "manuals/manual_list.html"
    context_object_name = "manuals"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")

        if query:
         queryset = queryset.filter(
        Q(title__icontains=query) |
        Q(category__icontains=query)
    )

        return queryset


class ManualDetailView(DetailView):
    model = Manual
    template_name = "manuals/manual_detail.html"
    context_object_name = "manual"

# Create your views here.
