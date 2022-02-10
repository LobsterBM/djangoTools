from django.db import models

# Create your models here.

class ModuleItem(models.Model):
    title = models.CharField(max_length=50)
    height = models.IntegerField
    width = models.IntegerField
    moduleID = models.AutoField

    def __str__(self):
        return self.title
