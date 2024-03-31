import requests

def scrape_data(region, parameter):
    url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/date/{region}.txt"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None



















# management/commands/create_metoffice_settings.py

# from django.core.management.base import BaseCommand
# from .models import MetOfficeDataSettings

# class Command(BaseCommand):
#     help = 'Create Met Office Data Settings'

#     def handle(self, *args, **kwargs):
#         parameters_choices = [choice[0] for choice in MetOfficeDataSettings.PARAMETERS_CHOICES]
#         region_choices = [choice[0] for choice in MetOfficeDataSettings.REGION_CHOICES]
#         data_choices = [choice[0] for choice in MetOfficeDataSettings.DATA_CHOICES]

#         for parameter in parameters_choices:
#             for region in region_choices:
#                 for data_type in data_choices:
#                     MetOfficeDataSettings.objects.create(parameters=parameter, region=region, data_type=data_type)



# import requests
# from io import StringIO
# import csv
# from django.utils import timezone
# from .models import Region, Year, Month, Parameters, MonthMasterTable

# # Define a function to fetch and parse the data
# def scrape_and_store_data(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         # Assuming the data is in CSV format
#         data = response.text

#         # Use StringIO to convert the string data into a file-like object
#         csv_file = StringIO(data)

#         # Use CSV reader to parse the data
#         csv_reader = csv.reader(csv_file, delimiter=',')
        
#         # Skip the header row if necessary
#         next(csv_reader)

#         # Iterate through each row in the CSV data
#         for row in csv_reader:
#             # Extract relevant information from the row
#             region_name = "Northern Ireland"  # Assuming this is the region for the provided URL
#             year_value = int(row[0])
#             month_name = row[1].lower()[:3]  # Assuming the month names are abbreviated
#             parameter_value = float(row[2])

#             # Retrieve or create Region instance
#             region, _ = Region.objects.get_or_create(name=region_name)

#             # Retrieve or create Year instance
#             year, _ = Year.objects.get_or_create(year=year_value)

#             # Retrieve or create Month instance
#             month, _ = Month.objects.get_or_create(name=month_name)

#             # Retrieve or create Parameter instance (if necessary)
#             parameter_name = "Air Frost"  # Assuming this is the parameter for the provided URL
#             parameter, _ = Parameters.objects.get_or_create(parameter=parameter_name)

#             # Create MonthMasterTable instance
#             month_master_instance = MonthMasterTable.objects.create(
#                 value=parameter_value,
#                 month=month,
#                 year=year,
#                 parameter=parameter,
#                 region=region
#             )

#             # Save the instance
#             month_master_instance.save()

#         print("Data scraped and stored successfully!")
#     else:
#         print("Failed to fetch data from the URL")

# # URL to scrape data from
# url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/AirFrost/date/Northern_Ireland.txt"

# # Call the function to scrape and store data
# scrape_and_store_data(url)
