# Create your models here.
from django.db import models

class Grower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    property_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Plant(models.Model):
    grower = models.ForeignKey(Grower, on_delete=models.CASCADE, related_name='plants')
    plant_type = models.CharField(max_length=50, default='Mango')
    location = models.CharField(max_length=200)
    planting_date = models.DateField()

    def __str__(self):
        return f"{self.plant_type} at {self.location}"

class SurveillanceRecord(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='records')
    surveillance_date = models.DateTimeField()
    pest_or_disease = models.CharField(max_length=100)
    plant_part = models.CharField(max_length=50, choices=[
        ('leaves', 'Leaves'),
        ('fruit', 'Fruit'),
        ('stem', 'Stem'),
        ('roots', 'Roots')
    ])
    severity = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Record for {self.plant} on {self.surveillance_date}"