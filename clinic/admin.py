from django.contrib import admin
from .models import Referral

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'patient_age', 'urgency', 'doctor_name', 'practice', 'created_at')
    list_filter = ('urgency', 'created_at')
    search_fields = ('patient_name', 'doctor_name', 'practice', 'diagnosis')
    ordering = ('-created_at',)