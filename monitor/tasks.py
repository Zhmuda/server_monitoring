import requests
from django.utils.timezone import now
from datetime import timedelta
from .models import Server, ResourceData, Incident


def fetch_resource_data():
    servers = Server.objects.all()
    for server in servers:
        try:
            response = requests.get(f'http://{server.ip_address}/metrics', timeout=5)
            if response.status_code == 200:
                data = response.json()
                ResourceData.objects.create(
                    server=server,
                    cpu_usage=data.get('cpu', 0),
                    memory_usage=data.get('memory', 0),
                    disk_usage=data.get('disk', 0)
                )
        except requests.RequestException:
            pass


def monitor_resources():
    threshold_cpu = 85
    threshold_memory = 90
    threshold_disk = 95

    thirty_minutes_ago = now() - timedelta(minutes=30)
    two_hours_ago = now() - timedelta(hours=2)

    for server in Server.objects.all():
        cpu_mem_resources = ResourceData.objects.filter(server=server, timestamp__gte=thirty_minutes_ago)
        disk_resources = ResourceData.objects.filter(server=server, timestamp__gte=two_hours_ago)

        cpu_high = any(r.cpu_usage > threshold_cpu for r in cpu_mem_resources)
        mem_high = any(r.memory_usage > threshold_memory for r in cpu_mem_resources)
        disk_high = any(r.disk_usage > threshold_disk for r in disk_resources)

        if cpu_high:
            Incident.objects.create(server=server, type="CPU Overload",
                                    description="CPU usage exceeded 85% for 30 minutes")
        if mem_high:
            Incident.objects.create(server=server, type="Memory Overload",
                                    description="Memory usage exceeded 90% for 30 minutes")
        if disk_high:
            Incident.objects.create(server=server, type="Disk Overload",
                                    description="Disk usage exceeded 95% for 2 hours")
