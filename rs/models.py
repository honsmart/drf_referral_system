from django.db import models
from django.utils import timezone
from .utils import generate_ref_code
from django.core.validators import MinLengthValidator



class Users(models.Model):
     first_name = models.CharField(max_length=30,  )
     last_name = models.CharField(max_length=30, validators=[MinLengthValidator(2)])
     user_name = models.CharField(max_length=30, validators=[MinLengthValidator(2)])
     email = models.EmailField(max_length=255, validators=[MinLengthValidator(2)])
     refferal_ID = models.CharField(max_length=255, default=generate_ref_code(), unique=True)
     referal_balance = models.DecimalField(max_digits=10, default=0, decimal_places=2)
     total_referral_bonus_earned = models.DecimalField(max_digits=10, default=0, decimal_places=2)
     total_referral_bonus_withdraw = models.DecimalField(max_digits=10, default=0, decimal_places=2) 
     total_reffered = models.IntegerField(default=0, null=True)
     reffered_by = models.CharField(max_length=225, default="", null=True, blank=True)
     password = models.CharField(max_length=30, validators=[MinLengthValidator(2)])


class ReferralsHistory(models.Model):
    STATUS_CHOICES = (
        ('rewarded', 'Rewarded'),
        ('not_rewarded', 'Not Rewarded'),
    )
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    reffered_by = models.CharField(max_length=225)
    amount= models.PositiveIntegerField(default=0)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='')    