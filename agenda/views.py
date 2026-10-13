from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Contact
from .forms import ContactForm

class ContactListView(ListView):
    model = Contact
    template_name = 'agenda/contact_list.html'
    context_object_name = 'contacts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(email__icontains=q))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'agenda/contact_detail.html'
    context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'agenda/contact_form.html'
    success_url = reverse_lazy('agenda:contact_list')

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'agenda/contact_form.html'
    success_url = reverse_lazy('agenda:contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'agenda/contact_confirm_delete.html'
    success_url = reverse_lazy('agenda:contact_list')
