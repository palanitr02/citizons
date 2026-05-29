from django.urls import path

from .views import (
    PersonListView,
    PersonCreateView,
    PersonDetailView,
    PersonUpdateView,
    PersonDeleteView
)

urlpatterns = [
    path("", PersonListView.as_view(), name="person_list"),
    path("create/", PersonCreateView.as_view(), name="person_create"),
    path("<int:pk>/", PersonDetailView.as_view(), name="person_detail"),
    path("<int:pk>/update/", PersonUpdateView.as_view(), name="person_update"),
    path("<int:pk>/delete/", PersonDeleteView.as_view(), name="person_delete"),
]