from django.db import models
from datetime import datetime,timedelta
import uuid

class Students(models.Model):
    roll_number = models.CharField(max_length=100,unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Guardian_name=models.CharField(max_length=100,help_text="parent/guardian full name")
    Email=models.EmailField(max_length=100,help_text="Guardian/parent e-mail")
    phone=models.IntegerField(null=True)
    def __str__(self):
        return self.fullname


class issue_book(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    issue_date=models.DateField(null=True)
