from django.db import models

class Referral(models.Model):
    URGENCY_CHOICES = [
        ('Routine', 'Routine'),
        ('Urgent', 'Urgent'),
        ('Emergency', 'Emergency'),
    ]

    patient_name = models.CharField(max_length=200)
    patient_age = models.IntegerField()
    diagnosis = models.TextField(help_text="Diagnosis / problem")
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, default='Routine')
    xray_link = models.URLField(blank=True, help_text="Link to X-rays if available")
    doctor_name = models.CharField(max_length=200)
    practice = models.CharField(max_length=200)
    doctor_contact = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.urgency} - {self.doctor_name}"