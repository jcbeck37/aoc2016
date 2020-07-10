from django.db import models

class Directions(models.Model):
    """ Direction of initial 90 degree rotation and Distance to travel """
    rotation = models.CharField(max_length=1)
    distance = models.IntegerField()

    def __str__(self):
        return self.rotation + str(self.distance)

class Coordinates(models.Model):
    """ Relative position from starting point (measured in Blocks) """
    xCoord = models.IntegerField()
    yCoord = models.IntegerField()

    def __str__(self):
        return str(self.xCoord) + ', ' + str(self.yCoord)
