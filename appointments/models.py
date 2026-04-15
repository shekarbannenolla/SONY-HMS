from django.db import models   # ✅ FIXED


class Appointment(models.Model):
    patients = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    appointment_status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.patients} - {self.doctor}"