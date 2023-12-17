from django.db import models

# Create your models here.

class CapitalCity(models.Model):
    cityname = models.CharField(max_length = 50)
    strength = models.IntegerField()
    
    def __str__(self) -> str:
        return self.cityname
    
class Country(models.Model):
    name = models.CharField(max_length = 100)
    language = models.CharField(max_length = 20)
    capital_city = models.OneToOneField(
        CapitalCity,
        on_delete = models.CASCADE,
        related_name = 'countries',
        related_query_name = 'country'
    )
    
    def __str__(self) -> str:
        return f'{self.name} : {self.capital_city}'