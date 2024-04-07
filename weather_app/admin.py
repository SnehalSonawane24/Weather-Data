from django.contrib import admin
from .models import AnnualData, FinalTotal, Region,RepeatingFields, Season, SeasonalData, Year, Month, MonthlyData, Parameter

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
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


@admin.register(FinalTotal)
class FinalTotalAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MonthlyData)
class MonthlyDataAdmin(admin.ModelAdmin):
    list_display = ('year','region','params','month','value')
    list_filter =( ('region', admin.RelatedOnlyFieldListFilter), ('params', admin.RelatedOnlyFieldListFilter), ('year', admin.RelatedOnlyFieldListFilter) )  # Uncomment this line to enable filtering by region
    search_fields = ('year',)
    fields = ('year', 'region', 'params', 'month', 'value')  # Define the order of fields

    # list_filter = ('year', 'params', 'region', 'month')


@admin.register(SeasonalData)
class SeasonalDataAdmin(admin.ModelAdmin):
    list_display = ('year','region','params','season','value')
    list_filter =( ('region', admin.RelatedOnlyFieldListFilter), ('params', admin.RelatedOnlyFieldListFilter), ('season', admin.RelatedOnlyFieldListFilter) )  # Uncomment this line to enable filtering by region
    search_fields = ('value',)
    fields = ('year', 'region', 'params', 'season', 'value')  # Define the order of fields
    # list_filter = ('year', 'params', 'region', 'season')


@admin.register(AnnualData)
class AnnualDataAdmin(admin.ModelAdmin):
    list_display = ('year','region','params','name','value')
    list_filter =( ('region', admin.RelatedOnlyFieldListFilter), ('params', admin.RelatedOnlyFieldListFilter), ('year', admin.RelatedOnlyFieldListFilter) )  # Uncomment this line to enable filtering by region

    fields = ('year', 'region', 'params', 'name', 'value')  # Define the order of fields
    # list_filter = ('year', 'params', 'region',)





















# @admin.register(Season)
# class SeasonAdmin(admin.ModelAdmin):
#     list_display = ('name',)


# @admin.register(MasterTable)
# class MasterTableAdmin(admin.ModelAdmin):
#     list_display = ('value', 'year', 'parameter', 'region', 'month', 'season')
#     list_filter = ('year', 'parameter', 'region', 'month', 'season')
#     search_fields = ('value',)

# @admin.register(Seasonaldata)
# class SeasonaldataAdmin(admin.ModelAdmin):
#     list_display = ('year', 'region', 'params', 'win', 'spr', 'sum','aut')
#     list_filter =( ('region', admin.RelatedOnlyFieldListFilter), ('params', admin.RelatedOnlyFieldListFilter) )  # Uncomment this line to enable filtering by region
#     search_fields = ('region',)

# admin.site.register(Seasonaldata)
# @admin.register(SeasonalData2)
# class SeasonalData2Admin(admin.ModelAdmin):
#     list_display = ('year', 'region', 'params', 'season','value')
#     list_filter =( ('region', admin.RelatedOnlyFieldListFilter), ('params', admin.RelatedOnlyFieldListFilter), )  # Uncomment this line to enable filtering by region
#     # search_fields = ('region',)


# @admin.register(SeasonalData2)
# class SeasonalData2Admin(admin.ModelAdmin):
#     list_display = ["year", "region", "params", "season", "value"]
#     list_filter = ["params", "region",]
    # list_filter = (("region", admin.RelatedOnlyFieldListFilter), )
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