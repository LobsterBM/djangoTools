from django.db import models
from colorfield.fields import ColorField


# Create your models here.

class ModuleItem(models.Model):
    title = models.CharField(max_length=50)
    height = models.IntegerField
    width = models.IntegerField
    moduleID = models.AutoField
    color = ColorField(default='#FF0000')



    def __str__(self):
        return self.title
class ColorPicker(models.Model):
    color = ColorField(default='#FF0000')

