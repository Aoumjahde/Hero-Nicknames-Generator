from django.db import models
import heroes

# Create your models here.


class Generat_Name(models.Model):

    def Generate_Name():
        name =  heroes.gen(1)
        return name

    
        pass