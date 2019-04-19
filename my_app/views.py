from django.shortcuts import render
from my_app.models import Shelter, Dog
from django.views.generic import (TemplateView, ListView)


# Create your views here.
class IndexView(TemplateView):
    dogs = Dog.objects.all()

    extra_context = {'dogs': dogs}
    template_name = 'my_app/index.html'


class ShelterListView(ListView):

    context_object_name = "shelters"
    model = Shelter


class DogListView(ListView):

    context_object_name = "dogs"
    model = Dog


