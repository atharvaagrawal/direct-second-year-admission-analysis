from django.urls import path
from . import views

urlpatterns = [
    path('Show-Seat-Matrix/',views.show_seat_matrix,name="show_seat_matrix")
]
