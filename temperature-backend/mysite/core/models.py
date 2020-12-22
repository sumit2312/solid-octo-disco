from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=1)

    def __str__(self):
        return str(self.name)


class Temperature(models.Model):
    temperature = models.FloatField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.temperature)


class Location(models.Model):
    location = models.CharField(max_length=50)
    location_long_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location


class Record(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return 'Temperature: ' + self.temperature.__str__() + \
            'Location: ' + self.location.__str__() + \
            'Date: ' + self.pub_date.__str__()