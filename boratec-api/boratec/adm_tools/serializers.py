from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from .models import PurchaseRequest

class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = [
            "id", 
            "request_id", 
            "date", 
            "status", 
            "company", 
            "branch_id", 
            "branch", 
            "category", 
            "requester", 
            "requester_email", 
            "department", 
            "payment_method", 
            "responsible",
            "deadline",
            "due_date",
            "pub_date",
            "obs",
            "attachment",
            "author",
            "last_update",
            "paid",
            ]