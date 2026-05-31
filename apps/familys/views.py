from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
from django.views.generic import *
from .models import *

class FamilyMemberCreateView(CreateView):
    model = FamilyMember
    fields = [
        "family",
        "person",
        "is_head",
        "joined_date",
    ]
    template_name = "family/member_form.html"
    success_url = reverse_lazy("family-list")



class FamilyUpdateView(UpdateView):
    model = Family
    fields = [
        "ration_card_no",
        "family_name",
        "district",
        "state",
        "pincode",
    ]
    template_name = "family/family_update.html"
    success_url = reverse_lazy("family-list")


    def form_valid(self, form):

        messages.success(self.request, "family updated successfully")

        return super().form_valid(form)



class FamilyCreateView(CreateView):
    model = Family
    fields = [
        "ration_card_no",
        "family_name",
        "district",
        "state",
        "pincode",
    ]
    template_name = "family/family_form.html"
    success_url = reverse_lazy("family-list")



class FamilyDetailView(DetailView):
    model = Family
    template_name = "family/family_detail.html"
    context_object_name = "family"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["members"] = self.object.familymember_set.select_related(
            "person"
        )

        return context
    


class FamilyListView(ListView):
    model = Family
    template_name = "family/family_list.html"
    context_object_name = "page_obj"
    paginate_by = 10
    ordering = ["-id"]

    def get_queryset(self):
        query = self.request.GET.get("q")

        queryset = Family.objects.all().order_by("-id")

        if query:
            queryset = queryset.filter(
                family_name__icontains=query
            )

        return queryset