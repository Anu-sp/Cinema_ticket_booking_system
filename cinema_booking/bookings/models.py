from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    name = models.CharField(max_length=100)
    screen = models.CharField(max_length=10)
    duration = models.DurationField()
    no_of_plays = models.IntegerField()
    start_time = models.DateTimeField()
    total_no_of_tickets = models.IntegerField()
    available_tickets = models.IntegerField()
    sold_tickets = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.name}'

