from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Movie, Booking
from .serializers import MovieSerializer, BookingSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .serializers import UserRegistrationSerializer
from collections import defaultdict
from rest_framework.response import Response
from rest_framework.views import APIView


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

class BookingListAPIView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        combined_bookings = defaultdict(lambda: {'seats_booked': 0, 'booking_time': None, 'screen': None})
        
        for booking in queryset:
            combined_bookings[booking.movie_id]['movie'] = booking.movie.id
            combined_bookings[booking.movie_id]['seats_booked'] += booking.seats_booked
            combined_bookings[booking.movie_id]['booking_time'] = booking.booking_time
            combined_bookings[booking.movie_id]['screen'] = booking.movie.screen  # Assuming the movie has a screen field
        
        return Response(list(combined_bookings.values()))

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookingCancelView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        movie = instance.movie
        seats = instance.seats_booked

        movie.available_tickets += seats
        movie.sold_tickets -= seats
        movie.save()

        instance.delete()

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Client-side token removal is recommended
        return Response({"detail": "Logged out successfully"}, status=204)