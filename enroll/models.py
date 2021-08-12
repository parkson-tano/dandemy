from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from courses.models import Course
# Create your models here.

ORDER_STATUS = (
		('Order Received', 'Order Received'),
		('Order Processing',  'Order Processing'),
		('On the way', 'On the way'),
		('Order Complete', 'Order Complete'),
		('Order Cancel', 'Order Cancel'),
	)

PAYMENT_METHOD = (
	("Cash On Delivery", "Cash On Delivery"),
	('Mobile Money', 'Mobile Money'),

)

class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    order_status = models.CharField(max_length=40, choices=ORDER_STATUS, default='Order Received')
    payment_method = models.CharField(max_length=40, choices=PAYMENT_METHOD, default='Mobile Money')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart.user + " order"