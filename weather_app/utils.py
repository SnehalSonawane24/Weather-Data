import requests
import pandas as pd



def scrape_data(region, parameter):
    url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/date/{region}.txt"
    response = requests.get(url)
    if response.status_code == 200:
        df = pd.read_fwf(url, colspecs='infer', widths=None, infer_nrows=100, skiprows=5)

        return df
    else:
        return None

















