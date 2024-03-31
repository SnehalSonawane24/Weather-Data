from django.shortcuts import render
from .models import MasterTable, Region, Parameter, Seasonaldata

from django.http import JsonResponse


from django.db.models.signals import post_migrate
from .utils import scrape_data
from django.db.utils import IntegrityError
from django.dispatch import receiver
from django.db.models import Min, Max, Avg



def fetch_data_view(request):
    regions = Region.objects.all()
    parameters = Parameter.objects.all()

    for region in regions:
        for parameter in parameters:
            data = scrape_data(region.name, parameter.name)
            if data is None:
                print(f"Failed to retrieve data for {region.name} - {parameter.name}")
                continue

            lines = data.strip().split('\n')
            if len(lines) < 7:
                print(f"Invalid data format for {region.name} - {parameter.name}")
                continue

            years = []
            seasonal_data_dict = {}  # Store seasonal data for each year

            # Extract years and corresponding seasonal data
            for line in lines[6:]:
                parts = line.split()
                if len(parts) < 7:
                    print(f"Invalid data format for {region.name} - {parameter.name}")
                    continue
                year = int(parts[0])
                years.append(year)
                seasonal_data_dict[year] = parts[1:]
                print("at line 43", seasonal_data_dict)
            years = sorted(years, reverse=True)

            # Save the years to the database
            for year in years:
                try:
                    # Get or create the Year object
                    year_obj, _ = Year.objects.get_or_create(year=year)
                    # Year.objects.get_or_create(year=year)
                    
                    # Get seasonal data for the current year
                    seasonal_data = seasonal_data_dict.get(year)
                    print("at line 53", year, seasonal_data)

                    if seasonal_data and len(seasonal_data) >= 16:  # Ensure there are enough elements in seasonal_data
                        
                        seasonal_data = [None if value == '---' else value for value in seasonal_data]
                        
                        seasonaldata, created = Seasonaldata.objects.update_or_create(
                            year=year_obj,
                            region=region,
                            params=parameter,
                            defaults={
                                'win': seasonal_data[12],
                                'spr': seasonal_data[13],
                                'sum': seasonal_data[14],
                                'aut': seasonal_data[15]
                            }
                        )
                        
                        
                    else:
                        print(f"No seasonal data found for year {year} in {region.name} - {parameter.name}")

                except IntegrityError as e:
                    print(f"Error creating year {year}: {e}")

            print("Seasonaldata saved successfully.")
    return render(request, 'home.html')



def create_month_choices():
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    print("month",months)
    for month in months:
        Month.objects.get_or_create(name=month)




# Connect the function to the post_migrate signal
@receiver(post_migrate)
def post_migrate_handler(sender, **kwargs):
    if sender.name == 'weather_app':
        print('weather-app')
        create_month_choices()  # Call the function to create Month objects


        



# season wise data 
from django.shortcuts import render
from .models import Region, Parameter, Seasonaldata

def fetch_data_view(request):
    regions = Region.objects.all()
    parameters = Parameter.objects.all()
    seasonal_data = Seasonaldata.objects.all()  # Fetch all seasonal data

    context = {
        'regions': regions,
        'parameters': parameters,
        'seasonal_data': seasonal_data  # Pass the seasonal data to the template
    }

    return render(request, 'home.html', context)


#month wise data

from django.http import JsonResponse

def fetch_filtered_data(request):
    region_id = request.GET.get('region')
    year = request.GET.get('year')
    parameter_id = request.GET.get('parameter')

    # Fetch data for the selected region, year, and parameter
    filtered_data = MasterTable.objects.filter(
        region_id=region_id,
        year_id=year,
        parameter_id=parameter_id
    ).values('region__name', 'parameter__name', 'year__year', 'month__name', 'value')

    return JsonResponse(list(filtered_data), safe=False)
