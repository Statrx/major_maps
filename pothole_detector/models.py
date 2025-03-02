
from django.db import models

class Pothole(models.Model):

    MINOR = 'minor'
    MODERATE = 'moderate'
    SEVERE = 'severe'

    SEVERITY_CHOICES = [
        (MINOR, 'Minor'),
        (MODERATE, 'Moderate'),
        (SEVERE, 'Severe'),
    ]


    latitude = models.FloatField()
    longitude = models.FloatField()
    severity = models.CharField(
        max_length=10,
        choices=SEVERITY_CHOICES,
        default=MODERATE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'pothole_detector_pothole'  
        managed = False  

    def __str__(self):
        return f"Pothole at ({self.latitude}, {self.longitude})"

