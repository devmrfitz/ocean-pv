from django.urls import path

from .views import (
    single_result_view,
    multiple_result_view, 
    IndividualResultView
)
from .json_views import update_accuracy

app_name = 'graphs'

urlpatterns = [
    path('<int:pk>/', IndividualResultView.as_view(), name='single_result'),
    path('multiple/', multiple_result_view, name='multiple_results'),
    path('update-accuracy/', update_accuracy, name='update-accuracy'),
]
