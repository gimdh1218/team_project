from django.db import models

# Create your models here.
class Gift(models.Model):
    image = models.ImageField(upload_to='imgaes/')
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.TextField()