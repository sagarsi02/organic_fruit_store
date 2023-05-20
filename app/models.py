from django.db import models
from django.utils import timezone  
import uuid


ltr_or_kg = (('Kg', 'Kg'), ('Liter', 'Liter'))
class product(models.Model):
    product_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4
    )
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    price = models.IntegerField()
    image = models.ImageField(upload_to='prod_img/')
    kg_or_ltr = models.CharField(
        max_length = 5,
        choices = ltr_or_kg,
        default='Kg'
    )

class cart(models.Model):
    product_id = models.CharField(max_length=100, null=False, blank=False)
    user_id = models.CharField(max_length=50)
    product_quentity = models.IntegerField(default=1)


order_details = (
    ("Order Receive", "Order Receive"), 
    ("Order Packed", "Order Packed"), 
    ("Order Out for Delivery", "Order Out for Delivery"), 
    ("Order Delivered", "Order Delivered"), 
)

class orderdetails(models.Model):
    product_id_with_questity = models.CharField(max_length=250, null=False, blank=False)
    user_id = models.CharField(max_length=50, null=False, blank=False)
    total_fare = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    pincode = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    order_id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    date_time = models.DateTimeField(timezone.now())
    order_status = models.CharField(max_length = 50, choices = order_details, default = 'Order Receive')



