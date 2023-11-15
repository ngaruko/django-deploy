from django.db import models
class Entries(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)



