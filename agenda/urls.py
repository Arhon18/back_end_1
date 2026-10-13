from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('search/', views.ContactListView.as_view(), name='contact_search'),  # uses query param q
    path('add/', views.ContactCreateView.as_view(), name='contact_add'),
    path('<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('<int:pk>/edit/', views.ContactUpdateView.as_view(), name='contact_edit'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
]
