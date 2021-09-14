from django.db import models

class Laptop(models.Model):
    laptop_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    ram = models.IntegerField()
    rom = models.IntegerField()
    price = models.FloatField()
    processor = models.CharField(max_length=50)

    def __str__(self):
        return self.laptop_name