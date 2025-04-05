from django.urls import path
from.import views
urlpatterns = [
    path('sport/', views.AllSport, name='sport' ),
]
