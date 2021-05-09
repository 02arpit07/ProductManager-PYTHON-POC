from django.urls import path, include
from application_1.api import views
from rest_framework.routers import DefaultRouter
from application_1.api.views import ProductAPIView,ProductDetails


urlpatterns = [
    # path('product/', product_list),
    path('product/', ProductAPIView.as_view()),
    path('detail/<int:id>/', ProductDetails.as_view()),
]
