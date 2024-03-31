from django.contrib import admin
from .models import Region, Year, Month, Season, Parameter, MasterTable,Seasonaldata

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MasterTable)
class MasterTableAdmin(admin.ModelAdmin):
    list_display = ('value', 'year', 'parameter', 'region', 'month', 'season')
    list_filter = ('year', 'parameter', 'region', 'month', 'season')
    search_fields = ('value',)

@admin.register(Seasonaldata)
class SeasonaldataAdmin(admin.ModelAdmin):
    list_display = ('year', 'region', 'params', 'win', 'spr', 'sum','aut')
    # list_filter = ('year', 'parameter', 'region', 'month', 'season')
    search_fields = ('region',)

# admin.site.register(Seasonaldata)



# from django.contrib import admin

# # Register your models here.

# from .models import(
#     Region,
#     Year,
#     Month,
#     Season,
#     Parameters,
#     MonthMasterTable,
#     SeasonMasterTable,
#     AnnualMasterTable,
#     Answer
# )

# @admin.register(Region)
# class RegionAdmin(admin.ModelAdmin):
#     list_display = ["id", "name"]

# @admin.register(Year)
# class YearAdmin(admin.ModelAdmin):
#     list_display = ["id", "year"]

# @admin.register(Month)
# class MonthAdmin(admin.ModelAdmin):
#     list_display = ["id", "name"]

# @admin.register(Season)
# class SeasonAdmin(admin.ModelAdmin):
#     list_display = ["id", "name"]

# @admin.register(Parameters)
# class ParameterAdmin(admin.ModelAdmin):
#     list_display = ["id", "parameter"]


# @admin.register(MonthMasterTable)
# class MonthMasterTableAdmin(admin.ModelAdmin):
#     list_display = ["id", "value", "month", "year", "parameter", "region"]

# @admin.register(SeasonMasterTable)
# class SeasonMasterTableAdmin(admin.ModelAdmin):
#     list_display = ["id", "value", "year", "parameter", "region", "season"]

# @admin.register(AnnualMasterTable)
# class AnnualMasterTableAdmin(admin.ModelAdmin):
#     list_display = ["id", "value", "year", "region", "parameter"]


# admin.site.register(Answer)