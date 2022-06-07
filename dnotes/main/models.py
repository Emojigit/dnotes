from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import string, random

# Create your models here.

def randomword(length: int):
   letters = string.ascii_letters
   return ''.join(random.choice(letters) for i in range(length))

def ran10():
    return randomword(10)

class Note(models.Model):
    tid = models.CharField(max_length=10, primary_key=True, default=ran10)
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,editable=False)
    modify_on = models.DateTimeField(auto_now=True,editable=False)
    link_share = models.BooleanField(default=False)
    monospace = models.BooleanField(default=False)
    def __str__(self):
        return self.title + " by " + self.owner.username


