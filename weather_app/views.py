from django.shortcuts import render
from .models import MasterTable, Month, Region, Parameter, Seasonaldata, Year

from django.http import JsonResponse

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
