from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True) # blank=True means that this field is optional
    created = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that the date and time will be added automatically
    datecompleted = models.DateTimeField(null=True, blank=True) # null=True means that this field can be null, blank=True means that this field is optional
    important = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE) # on_delete=models.CASCADE means that if the user is deleted, all the todos associated with that user will also be deleted

    def __str__(self):
        return self.title
    