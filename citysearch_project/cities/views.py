from django.db.models import Q
from django.views.generic import TemplateView, ListView

from .models import Flightroute, Flight, Monthlyflight, Airport, Flightplane, Flightlist
from django.http import HttpResponseRedirect
from django.shortcuts import render

# from .forms import NameForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Flightroute
    template_name = 'search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Flightroute.objects.filter(
            Q(month__icontains=query) | Q(origin_city__icontains=query)
        )
        return object_list

class SearchPlaneResultsView(ListView):
    model = Flightplane
    template_name = 'search_plane.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Flightplane.objects.filter(
            Q(month__icontains=query) | Q(origin_city__icontains=query)
        )
        return object_list

class SearchMonthResultsView(ListView):
    model = Monthlyflight
    template_name = 'search_month.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Monthlyflight.objects.filter(
            Q(month__icontains=query)
        )
        return object_list

class SearchFlightResultsView(ListView):
    model = Flight
    template_name = 'search_flight.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Flight.objects.filter(
            Q(origin__icontains=query)
        )
        return object_list

class SearchAirportResultsView(ListView):
    model = Airport
    template_name = 'search_airport.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Airport.objects.filter(
            Q(city__icontains=query) | Q(icao__icontains=query)
        )
        return object_list