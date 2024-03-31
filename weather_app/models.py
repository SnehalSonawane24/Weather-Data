from django.db import models
# from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Region(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name

class Parameter(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
    
class Year(models.Model):
    year = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural = "Years"
        ordering = ['-year'] 

    def __str__(self):
        return str(self.year)
    
class Seasonaldata(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    params = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    win = models.FloatField(max_length=25,null=True, blank=True)
    spr = models.FloatField(max_length=25,null=True, blank=True)
    sum = models.FloatField(max_length=25,null=True, blank=True)
    aut = models.FloatField(max_length=25,null=True, blank=True)
    
    def get_season_name(self, season):
        if season == 'win':
            return 'Winter'
        elif season == 'spr':
            return 'Spring'
        elif season == 'sum':
            return 'Summer'
        elif season == 'aut':
            return 'Autumn'
        else:
            return season

    

class Month(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Seasons"

    def __str__(self):
        return self.name




class MasterTable(models.Model):
    value = models.FloatField(null=True, blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name="year_master")
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, related_name="parameter_master")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="region_master")
    month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name="month_master", null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="season_master", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Master Tables"

    def __str__(self):
        return str(self.value)
