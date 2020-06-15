from django.urls import path
from .views import (
    single_result_view,
    multiple_result_view,
)

app_name = 'graphs'

urlpatterns = [
    path('<int:pk>/', single_result_view, name='single_result'),
    path('multiple/', multiple_result_view, name='multiple_results'),

]
