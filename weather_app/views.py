from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from requests import request
from .models import AnnualData, FinalTotal, MonthlyData, Region, Parameter, Season, SeasonalData, Year,Month
from .utils import scrape_data
from django.db.utils import IntegrityError
from django.dispatch import receiver
import pandas as pd
from django.core.paginator import Paginator
from django.http import JsonResponse


def fetch_data_view(request):
    yearly_monthly_data_dict = {}
    regions = Region.objects.all()
    parameters = Parameter.objects.all()

    
   
    selected_region_name = None
    selected_parameter_name = None

    if 'region' in request.GET and 'parameter' in request.GET:
        
        selected_region_name = request.GET['region']
        selected_parameter_name = request.GET['parameter']

        selected_region = Region.objects.get(name=selected_region_name)
        selected_parameter = Parameter.objects.get(name=selected_parameter_name)

        data = scrape_data(selected_region.name, selected_parameter.name)
        if data is not None:
            data.replace("---", None, inplace=True)
            data.fillna("", inplace=True)
            for year, row in data.iterrows():
                year = row['year']
                yearly_monthly_data_dict.setdefault(year, {})
                for month_name in data.columns[1:-5]: 
                    month = Month.objects.update_or_create(name=month_name)[0]
                    year_obj, created = Year.objects.update_or_create(year=int(row['year']))

                    value = row[month_name]
                    if isinstance(value, str) and value.strip() == '':
                        print(f"Empty value for {month_name} in year {year}")
                        continue
                    try:
                        value = float(value)
                    except ValueError:
                        print(f"Invalid value '{value}' for {month_name} in year {year}")
                        continue

                    monthly_data, created = MonthlyData.objects.update_or_create(
                        year=year_obj,
                        region=selected_region,
                        params=selected_parameter,
                        month=month,
                        defaults={'value': row[month_name]}
                    )
                    
                    yearly_monthly_data_dict[year].setdefault(month_name, {})
                    yearly_monthly_data_dict[year][month_name] = value

                for season_name in data.columns[-5:-1]:  
                    season = Season.objects.update_or_create(name=season_name)[0]

                    value = row[season_name]
                    if isinstance(value, str) and value.strip() == '':
                        print(f"Empty value for {season_name} in year {year}")
                        continue
                    try:
                        value = float(value)
                    except ValueError:
                        print(f"Invalid value '{value}' for {season_name} in year {year}")
                        continue

                    seasonal_data, created = SeasonalData.objects.update_or_create(
                        year=year_obj,
                        region=selected_region,
                        params=selected_parameter,
                        season=season,
                        defaults={'value': value}
                    )

                    yearly_monthly_data_dict[year].setdefault(season_name, {})
                    yearly_monthly_data_dict[year][season_name] = value

                for ann_name in data.columns[-1:]:  
                    name = FinalTotal.objects.update_or_create(name=ann_name)[0]

                    value = row[ann_name]
                    if isinstance(value, str) and value.strip() == '':
                        print(f"Empty value for {ann_name} in year {year}")
                        continue
                    try:
                        value = float(value)
                    except ValueError:
                        print(f"Invalid value '{value}' for {ann_name} in year {year}")
                        continue

                    annual_data, created = AnnualData.objects.update_or_create(
                        year=year_obj,
                        region=selected_region,
                        params=selected_parameter,
                        name=name,
                        defaults={'value': value}
                    )
                    
                    yearly_monthly_data_dict[year].setdefault(ann_name, {})
                    yearly_monthly_data_dict[year][ann_name] = value

    page_number = request.GET.get('page', 1)  
    page_size =10 
    sorted_data = sorted(yearly_monthly_data_dict.items(), key=lambda x: x[0], reverse=True)

    paginator = Paginator(sorted_data, page_size)
    page_obj = paginator.get_page(page_number)

    
    context = {
        'regions': regions,
        'parameters': parameters,
        'selected_region_id': selected_region_name,
        'selected_parameter_id': selected_parameter_name,
        'page_obj': page_obj,  
        'yearly_monthly_data': yearly_monthly_data_dict,
    }

    return render(request, 'data.html', context)



































# def fetch_data_view(request):
#     yearly_monthly_data_dict = {}

#     regions = Region.objects.all()
#     parameters = Parameter.objects.all()
#     for region in regions:
#         for parameter in parameters:
#             if region.name == "Scotland" and parameter.name == "Tmax" :    
#                 data = scrape_data(region.name, parameter.name)
#                 if data is not None:
#                     data.replace("---", None, inplace=True)
#                     data.fillna("", inplace=True)
#                     # print(data.to_string(index=False))
#                     for year, row in data.iterrows():
#                         year = row['year']
#                         yearly_monthly_data_dict.setdefault(year, {})
#                         for month_name in data.columns[1:-5]:  # Exclude the first column (year) and last 4 columns (seasonal and annual data)
#                             month = Month.objects.update_or_create(name=month_name)[0]
#                             year_obj, created = Year.objects.update_or_create(year=int(row['year']))

#                             # Handle empty or non-numeric values
#                             value = row[month_name]
#                             if isinstance(value, str) and value.strip() == '':
#                                 # If the value is empty, skip this data point
#                                 print(f"Empty value for {month_name} in year {year}")
#                                 continue
#                             try:
#                                 value = float(value)
#                             except ValueError:
#                                 # If the value is not a valid number, skip this data point
#                                 print(f"Invalid value '{value}' for {month_name} in year {year}")
#                                 continue
                            
#                             # Create or update MonthlyData instance
#                             monthly_data, created = MonthlyData.objects.update_or_create(
#                                 year=year_obj,
#                                 region=region,
#                                 params=parameter,
#                                 month=month,
#                                 defaults={'value': row[month_name]}
#                             )
                            
#                             yearly_monthly_data_dict[year].setdefault(month_name, {})
#                             yearly_monthly_data_dict[year][month_name] = value

#                             # if created:
#                             #     print("monthly_data Data saved successfully:", monthly_data)
#                             # else:
#                             #     print("Data updated:", monthly_data)


                        
#                         for season_name in data.columns[-5:-1]:  # Select the last four columns for seasonal data
#                             # print("////////////////",season_name)
#                             season = Season.objects.update_or_create(name=season_name)[0]
                            
#                             # Handle empty or non-numeric values
#                             value = row[season_name]
#                             if isinstance(value, str) and value.strip() == '':
#                                 # If the value is empty, skip this data point
#                                 print(f"Empty value for {season_name} in year {year}")
#                                 continue
#                             try:
#                                 value = float(value)
#                             except ValueError:
#                                 # If the value is not a valid number, skip this data point
#                                 print(f"Invalid value '{value}' for {season_name} in year {year}")
#                                 continue
                            
#                             # Create or update SeasonalData instance
#                             seasonal_data, created = SeasonalData.objects.update_or_create(
#                                 year=year_obj,
#                                 region=region,
#                                 params=parameter,
#                                 season=season,
#                                 defaults={'value': value}
#                             )

#                             yearly_monthly_data_dict[year].setdefault(season_name, {})
#                             yearly_monthly_data_dict[year][season_name] = value

                            
#                             # if created:
#                             #     print("seasonal_data Data saved successfully:", seasonal_data)
#                             # else:
#                             #     print("Data updated:", seasonal_data)

#                         for ann_name in data.columns[-1:]:  # Select the last columns for ann data
#                             # print("/////////",ann_name)
#                             name = FinalTotal.objects.update_or_create(name=ann_name)[0]
                            
#                             # Handle empty or non-numeric values
#                             value = row[ann_name]
#                             if isinstance(value, str) and value.strip() == '':
#                                 # If the value is empty, skip this data point
#                                 print(f"Empty value for {ann_name} in year {year}")
#                                 continue
#                             try:
#                                 value = float(value)
#                             except ValueError:
#                                 # If the value is not a valid number, skip this data point
#                                 print(f"Invalid value '{value}' for {ann_name} in year {year}")
#                                 continue
                            
#                             # Create or update SeasonalData instance
#                             annual_data, created = AnnualData.objects.update_or_create(
#                                 year=year_obj,
#                                 region=region,
#                                 params=parameter,
#                                 name=name,
#                                 defaults={'value': value}
#                             )
                            
                        
#                             yearly_monthly_data_dict[year].setdefault(ann_name, {})
#                             yearly_monthly_data_dict[year][ann_name] = value

                            

#                             # if created:
#                             #     print("Annual_data Data saved successfully:", annual_data)
#                             # else:
#                             #     print("Data updated:", annual_data)

                    
                       
#                 else:
#                     print("Failed to fetch data for region:", region, "and parameter:", parameter)
#                     continue
#             else:
#                 print("Skipping data fetch for region:", region, "and parameter:", parameter)


#     print("///////////",yearly_monthly_data_dict)
#     # return HttpResponse("fetch success")
#     # return show_data(request, yearly_monthly_data_dict)

#     page_number = request.GET.get('page', 1)  # Default to page 1
#     page_size = 50  # Number of items per page
#     paginator = Paginator(list(yearly_monthly_data_dict.items()), page_size)
#     page_obj = paginator.get_page(page_number)

    
#     return render(request, 'data.html', {'page_obj': page_obj})
















# from django.core.paginator import Paginator
# from django.shortcuts import render
# from django.db import transaction
# from .models import Region, Parameter, Month, Year, Season, FinalTotal, MonthlyData, SeasonalData, AnnualData

# @transaction.atomic
# def fetch_data_view(request):
#     regions = Region.objects.all().select_related('name')
#     parameters = Parameter.objects.all().select_related('name')

#     yearly_monthly_data_dict = {}

#     for region in regions:
#         for parameter in parameters:
#             data = scrape_data(region.name, parameter.name)
#             if data is not None:
#                 data.replace("---", None, inplace=True)
#                 data.fillna("", inplace=True)
#                 for _, row in data.iterrows():
#                     year_value = int(row['year'])
#                     year_obj, _ = Year.objects.get_or_create(year=year_value)
#                     process_monthly_data(year_obj, region, parameter, row, data.columns[1:-5], yearly_monthly_data_dict)
#                     process_seasonal_data(year_obj, region, parameter, row, data.columns[-5:-1], yearly_monthly_data_dict)
#                     process_annual_data(year_obj, region, parameter, row, data.columns[-1:], yearly_monthly_data_dict)

#             else:
#                 print("Failed to fetch data for region:", region, "and parameter:", parameter)

#     return render(request, 'home.html', {'yearly_monthly_data_dict': yearly_monthly_data_dict})


# def process_monthly_data(year_obj, region, parameter, row, data_columns, yearly_monthly_data_dict):
#     for month_name in data_columns:
#         month_obj, _ = Month.objects.update_or_create(name=month_name)
#         value = row[month_name]
#         if value.strip() == '':
#             continue
#         try:
#             value = float(value)
#         except ValueError:
#             continue
#         monthly_data, _ = MonthlyData.objects.update_or_create(
#             year=year_obj,
#             region=region,
#             params=parameter,
#             month=month_obj,
#             defaults={'value': value}
#         )
#         yearly_monthly_data_dict.setdefault(year_obj.year, {}).setdefault(month_name, value)


# def process_seasonal_data(year_obj, region, parameter, row, data_columns, yearly_monthly_data_dict):
#     for season_name in data_columns:
#         season_obj, _ = Season.objects.update_or_create(name=season_name)
#         value = row[season_name]
#         if value.strip() == '':
#             continue
#         try:
#             value = float(value)
#         except ValueError:
#             continue
#         seasonal_data, _ = SeasonalData.objects.update_or_create(
#             year=year_obj,
#             region=region,
#             params=parameter,
#             season=season_obj,
#             defaults={'value': value}
#         )
#         yearly_monthly_data_dict.setdefault(year_obj.year, {}).setdefault(season_name, value)


# def process_annual_data(year_obj, region, parameter, row, data_columns, yearly_monthly_data_dict):
#     for ann_name in data_columns:
#         name = FinalTotal.objects.update_or_create(name=ann_name)[0]
#         value = row[ann_name]
#         if isinstance(value, str) and value.strip() == '':
#             continue
#         try:
#             value = float(value)
#         except ValueError:
#             continue

#         annual_data, _ = AnnualData.objects.update_or_create(
#             year=year_obj,
#             region=region,
#             params=parameter,
#             name=name,
#             defaults={'value': value}
#         )
#         yearly_monthly_data_dict.setdefault(year_obj.year, {}).setdefault(ann_name, value)


# # Another function to process the data or perform additional tasks
# def another_function(yearly_monthly_data_dict):
#     # Perform operations on yearly_monthly_data_dict
#     print(yearly_monthly_data_dict)
#     # You can access and manipulate the data stored in yearly_monthly_data_dict here


# # Call fetch_data_view to populate yearly_monthly_data_dict
# yearly_monthly_data_dict_from_fetch = fetch_data_view(request)

# # Pass yearly_monthly_data_dict to another_function
# another_function(yearly_monthly_data_dict_from_fetch)











