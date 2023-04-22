from django.db import models
from django.conf import settings

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_budget = models.CharField(max_length=30)
    project_category = models.CharField(max_length=254)
    project_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_foto = models.CharField(max_length=100)
    project_users = models.CharField(max_length=100)
    project_creation_date = models.DateTimeField(auto_now_add=True)
    project_details = models.CharField(max_length=100)