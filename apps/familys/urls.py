from django.urls import path
from .views import (
    FamilyListView,
    FamilyDetailView,
    FamilyCreateView,
    FamilyUpdateView,
    FamilyMemberCreateView,
)

urlpatterns = [
    path(
        "families/",
        FamilyListView.as_view(),
        name="family-list"
    ),

    path(
        "families/create/",
        FamilyCreateView.as_view(),
        name="family-create"
    ),

    path(
        "families/<int:pk>/",
        FamilyDetailView.as_view(),
        name="family-detail"
    ),

    path(
        "families/<int:pk>/update/",
        FamilyUpdateView.as_view(),
        name="family-update"
    ),

    path(
        "family-members/create/",
        FamilyMemberCreateView.as_view(),
        name="family-member-create"
    ),
]