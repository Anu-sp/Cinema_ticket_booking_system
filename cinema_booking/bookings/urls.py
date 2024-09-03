from django.urls import path
from .views import (
    MovieListCreateView, MovieDetailView,
    BookingCancelView,UserRegistrationView,BookingListAPIView,BookingCreateAPIView,LogoutView,
)
from rest_framework_simplejwt.views import TokenObtainPairView,TokenBlacklistView,TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('bookings/', BookingListAPIView.as_view(), name='booking-list'),
    path('bookings/create/', BookingCreateAPIView.as_view(), name='booking-create'),
     path('bookings/<int:pk>/cancel/', BookingCancelView.as_view(), name='booking-cancel'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
