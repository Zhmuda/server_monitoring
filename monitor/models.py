from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class ResourceData(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    cpu = models.FloatField()
    mem = models.CharField(max_length=10)
    disk = models.CharField(max_length=10)
    uptime = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.server.name} - {self.timestamp}"

class Incident(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.server.name} - {self.timestamp}"