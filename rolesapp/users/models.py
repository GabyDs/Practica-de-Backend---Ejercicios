from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    # 0 -> usuario normal
    # 1 -> usuario admin
    rol = models.BooleanField(default=0)
