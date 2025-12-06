from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ChatMessage(models.Model):
    ROLE_CHOICES = (('user','User'),
                    ('assistant','Assistant'))
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
