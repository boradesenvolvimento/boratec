from django.urls import path

from . import views

urlpatterns = [
    path("purchase_request/", views.PurchaseRequest.as_view(), name="signup"),
]