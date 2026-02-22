from django.http import JsonResponse
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import MyTokenObtainPairView

def home(request):
    return JsonResponse({"message": "Auth Service is running"})

urlpatterns = [
    path('', home),
    path('api/', include('users.urls')),
    path('api/login/', MyTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

