from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages

from .models import Person

class PersonListView(ListView):

    model = Person
    template_name = "persons/person_list.html"
    context_object_name = "page_obj"
    paginate_by = 10
    ordering = ["-id"]

    def get_queryset(self):

        query = self.request.GET.get("q")

        queryset = Person.objects.all()

        if query:

            queryset = queryset.filter(
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query) |
                Q(adhar_num__icontains=query)
            )

        return queryset
    
class PersonCreateView(CreateView):

    model = Person
    template_name = "persons/person_create.html"

    fields = [
        "firstname",
        "lastname",
        "dob",
        "gender",
        "adhar_num",
        "father",
        "mother"
    ]

    success_url = reverse_lazy("person_list")

    def form_valid(self, form):

        messages.success(self.request, "Person created successfully")

        return super().form_valid(form)
    

class PersonDetailView(DetailView):

    model = Person
    template_name = "persons/person_detail.html"
    context_object_name = "person"

class PersonUpdateView(UpdateView):

    model = Person
    template_name = "persons/person_update.html"

    fields = [
        "firstname",
        "lastname",
        "dob",
        "gender",
        "adhar_num",
        "father",
        "mother"
    ]

    success_url = reverse_lazy("person_list")

    def form_valid(self, form):

        messages.success(self.request, "Person updated successfully")

        return super().form_valid(form)
    
class PersonDeleteView(DeleteView):

    model = Person
    template_name = "persons/person_delete.html"
    success_url = reverse_lazy("person_list")

    def delete(self, request, *args, **kwargs):

        messages.success(self.request, "Person deleted successfully")

        return super().delete(request, *args, **kwargs)
    
