from django.contrib.gis.db import models

class Plan(models.Model):
    name =  models.CharField(max_length=255)

    def __str__(self):
        return f"Plan {self.name}"

class Coverage(models.Model):

    address = models.CharField(max_length=255)
    color = models.CharField(blank=True, null=True, max_length=100)
    location = models.GeometryField(blank=True, null=True)
    plans = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plans')

    def __str__(self):
        return f"Cobertura {self.pk}"

    class Meta:
        db_table = "address"
        order_with_respect_to = "address"


