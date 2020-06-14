"""ocean_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from interactions.views import (
    HowtoView,
    self_question_list_view,
    relation_question_list_view
)

app_name = 'interactions'

urlpatterns = [
    path('howto/', HowtoView.as_view(template_name='interactions/howto_self.html'), name='howto'),
    path('howto/relations/', HowtoView.as_view(
        template_name='interactions/howto_relations.html'), name='howto-relations'),
    path('taketest/', self_question_list_view, name='taketest'),
    path('taketest/relations/', relation_question_list_view,
         name='taketest-relations'),
]
