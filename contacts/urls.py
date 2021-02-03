from django.urls import path
from contacts.views import ContactList, ContactDetailView

urlpatterns = [
    path('', ContactList.as_view(), name='list'),
    path('<id>', ContactDetailView.as_view(), name='detail'),
]