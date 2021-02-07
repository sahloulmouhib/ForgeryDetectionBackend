from django.db import models

# Create your models here.
class Client(models.Model):
    firstName= models.TextField()
    email=models.TextField()
    review=models.TextField()
    image = models.FileField(upload_to='images/',default='images/apple.jpg')
    