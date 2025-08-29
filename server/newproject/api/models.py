from django.db import models

# Create your models here.
# modela in django are how you db tables are gonna be created 

class book(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()


# define how this class will be represented
    def __str__(self):
        return self.title