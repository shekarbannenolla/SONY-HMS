from django.db import models

# Create your models here.
class  Appoinment (models.Model):
    patients = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    appoinment_time = models.DateTimeField()
    appoinment_staatus = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.patients} - {self.doctor}"