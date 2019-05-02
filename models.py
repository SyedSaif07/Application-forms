from django.db import models

class form(models.Model):
    name = models.CharField(max_length = 100,unique=True)
    fathername = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    city = models.CharField(max_length = 50)
    dob = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 10)
    course = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return self.name









        
