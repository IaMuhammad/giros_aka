from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import TypeAPIView, TableListAPIView, MealListAPIView, OrderCreateAPIView, OrderRetrieveAPIView

urlpatterns = [
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/types/', TypeAPIView.as_view(), name='types'),
    path('api/v1/tables/', TableListAPIView.as_view(), name='tables'),
    path('api/v1/meals/', MealListAPIView.as_view(), name='meals'),
    path('api/v1/order/', OrderCreateAPIView.as_view(), name='order'),
    path('api/v1/order/<int:pk>', OrderRetrieveAPIView.as_view(), name='order_detail'),
]
