
from django.urls import path
from .views import ManualListView, ManualDetailView

urlpatterns = [
    path("", ManualListView.as_view(), name="manual_list"),
    path("<int:pk>/", ManualDetailView.as_view(), name="manual_detail"),
]