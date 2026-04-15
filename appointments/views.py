from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment
# Create your views here.
@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'app_list.html', {'appointments': appointments})
    
    
