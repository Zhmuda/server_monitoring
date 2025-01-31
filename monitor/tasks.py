import requests
from .models import Server, ResourceData
from django.utils import timezone
from datetime import timedelta
from django.utils import timezone
from .models import ResourceData, Incident


def fetch_resource_data():
    servers = Server.objects.all()
    for server in servers:
        # Заглушка для тестирования
        response = {
            "cpu": 60,
            "mem": "30%",
            "disk": "43%",
            "uptime": "1d 2h 37m 6s"
        }
        ResourceData.objects.create(
            server=server,
            cpu=response['cpu'],
            mem=response['mem'],
            disk=response['disk'],
            uptime=response['uptime']
        )

def monitor_resources():
    servers = Server.objects.all()
    for server in servers:
        resources = ResourceData.objects.filter(server=server, timestamp__gte=timezone.now() - timedelta(minutes=30))
        cpu_high = all(resource.cpu > 85 for resource in resources)
        mem_high = all(float(resource.mem.strip('%')) > 90 for resource in resources)
        disk_high = all(float(resource.disk.strip('%')) > 95 for resource in resources)

        if cpu_high:
            Incident.objects.create(server=server, message="CPU usage exceeded 85% for 30 minutes")
        if mem_high:
            Incident.objects.create(server=server, message="Memory usage exceeded 90% for 30 minutes")
        if disk_high:
            Incident.objects.create(server=server, message="Disk usage exceeded 95% for 2 hours")