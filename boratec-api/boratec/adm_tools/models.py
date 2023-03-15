import datetime
from django.db import models
from .constants import STATUS_CHOICES, DEPARTMENT_CHOICES, PAYMENT_METHOD_CHOICES
from user.models import User
# Create your models here.
class PurchaseRequest(models.Model):

    id = models.BigAutoField(primary_key=True)
    request_id = models.CharField(max_length=10)
    date = models.DateField()
    status = models.CharField(max_length=15)
    company = models.CharField(max_length=2)
    branch_id = models.CharField(max_length=2, null=True, blank=True)
    branch = models.CharField(max_length=3)
    category = models.CharField(max_length=15)
    requester = models.CharField(max_length=100)
    requester_email = models.EmailField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=15, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES, blank=True, null=True)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='responsavelcompras')
    deadline = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    obs = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='cpr/%Y/%m/%d', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autorcompras')
    last_update = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ultimaattcompras',
                                   blank=True, null=True)
    paid = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.request_id
    
class ProductRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.CharField(max_length=200)
    itens_qty = models.IntegerField()
    solic_ref = models.ForeignKey(PurchaseRequest, on_delete=models.CASCADE)