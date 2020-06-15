from django.urls import path
from home.views import (
    HomeView,
    ResourcesView,
    ContactView,
    ContactDoneView
)

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('resources/', ResourcesView.as_view(), name='resources'),
    path('contact/done/', ContactDoneView.as_view(), name='contact-done'),
]
