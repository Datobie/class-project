from django.urls import path
from .views import *


urlpatterns = [
    path("", Product_page),
    path("<int:pk>/", product_detail_page, name="detail")
]