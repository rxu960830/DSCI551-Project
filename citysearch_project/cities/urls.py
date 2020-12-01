from django.urls import path

from .views import HomePageView, SearchResultsView,SearchMonthResultsView,SearchFlightResultsView,SearchAirportResultsView

urlpatterns = [
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('search_month/', SearchMonthResultsView.as_view(), name='search_month'),
    path('search_flight/', SearchFlightResultsView.as_view(), name='search_flight'),
    path('search_airport/', SearchAirportResultsView.as_view(), name='search_airport'),
    path('', HomePageView.as_view(), name='home'),
]