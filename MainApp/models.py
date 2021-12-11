from django.contrib.postgres.fields import ArrayField
from django_mysql.models import ListCharField
from django.db.models import CharField
from django.db import models
import random


#users role options
user_types = (
    ('SuperAdmin', 'SuperAdmin'),
    ('Admin','Admin'),
    ('Agent','Agent'))


#Users Model
class UsersModel(models.Model):
    user_type = models.CharField(max_length=50, choices=user_types, default='Admin')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


#get random serial no for product
def get_serialno():
    rnd_id = random.randint(100000, 999999)
    return rnd_id

class ProductsModel(models.Model):
    serial_no = models.CharField(max_length=50, default=get_serialno())
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    region = models.CharField(max_length=100)


#Multiple choices
call_actions = (
    ('Answered','Answered'),
    ('Rejected','Rejected'))

_approvals = (
    ('Initial', 'Initial'),
    ('Pending', 'Pending'),
    ('Approved', 'Approved'))

call_reasons = (
    ('Information', 'Information'),
    ('Inquiries', 'Inquiries'),
    ('Complaints', 'Complaints'),
    ('Support', 'Support'))


class CallLogsModel(models.Model):
    agent_idno =  models.CharField(max_length=10)
    serial_no = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=20)
    call_reason = models.CharField(max_length=200, choices=call_reasons, default='')
    remark = models.CharField(max_length=100)
    items = models.CharField(max_length=255)
    call_action = models.CharField(max_length=100, choices=call_actions, default='')
    approval = models.CharField(max_length=100, choices=_approvals, default='')
    call_date = models.DateField()