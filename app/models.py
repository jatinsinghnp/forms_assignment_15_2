from django.db import models

# Create your models here.
class model1(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=220)
    adress = models.CharField(max_length=220)

    def __str__(self) -> str:
        return str(self.id)+ " " + " " +self.name + " "+ self.adress
