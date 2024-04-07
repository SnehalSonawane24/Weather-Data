from django.db import models
from django.dispatch import receiver



class Region(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "5. Regions"

    def __str__(self):
        return self.name

class Parameter(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "6. Parameters"

    def __str__(self):
        return self.name
    
class Year(models.Model):
    year = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural = "4. Years"
        ordering = ['-year'] 

    def __str__(self):
        return f"{self.year}"
    



class RepeatingFields(models.Model):
    
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    params = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.FloatField()

    class Meta:
        abstract = True 
        
class Month(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "8. Months"

    def __str__(self):
        return self.name

class MonthlyDataManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('month', 'year', 'region', 'params')
  
    def for_year(self, year):
        return self.get_queryset().filter(year__year=year)
    
    
    

class MonthlyData(RepeatingFields):
   
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    objects = MonthlyDataManager()  


    class Meta:
        verbose_name_plural = "1. Monthly Data"

    def __str__(self):
        return f"{self.month.name} - {self.year.year}"





class Season(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "8. Seasons"

    def __str__(self):
        return f"{self.name}"

class SeasonalData(RepeatingFields):
    
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "2. Seasonal Data"

    def __str__(self):
        return str(self.season.name)
    




class FinalTotal(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = "7. FinalTotal"

    def __str__(self):
        return f"{self.name}"
    
class AnnualData(RepeatingFields):
    
    name = models.ForeignKey(FinalTotal, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "3. Annual Data"

    def __str__(self):
        return str(self.value)