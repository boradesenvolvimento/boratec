from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from .models import PurchaseRequest
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "admission", "phone", "first_name", "last_name"]

class PurchaseRequestSerializer(serializers.ModelSerializer):
    responsible = serializers.SlugRelatedField(slug_field='email', many=False, read_only=True)
    author = serializers.SlugRelatedField(slug_field='email', many=False, read_only=True)
    last_update = serializers.SlugRelatedField(slug_field='email', read_only=True)

    #responsible_id = UserSerializer(many=False)
    #author_id = UserSerializer(many=False)
    #last_update_id = UserSerializer(many=False)

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