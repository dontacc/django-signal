from django.db import models

# Create your models here.




class Students(models.Model):
    name = models.CharField(max_length=64)
    family = models.CharField(max_length=64)
    students_code = models.CharField(max_length=6)


    def __str__(self):
        return self.name