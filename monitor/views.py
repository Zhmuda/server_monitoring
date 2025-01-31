from django.shortcuts import render
from .models import Incident

def incident_list(request):
    incidents = Incident.objects.all().order_by('-timestamp')
    return render(request, 'monitor/incident_list.html', {'incidents': incidents})