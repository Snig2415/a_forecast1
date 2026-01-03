import requests
import pandas as pd
from io import StringIO

# OMNIWeb CGI request URL
# Parameters:
# - res=hour → 1-hour resolution
# - start_date / end_date → time range
# - vars → variables you want
# - format=ascii → ASCII output
url = (
    "https://omniweb.gsfc.nasa.gov/cgi/nx1.cgi?"
    "activity=retrieve&res=hour&start_date=2015-01-01&end_date=2025-12-31&"
    "vars=flow_speed,proton_density,bz_gsm,flow_pressure&format=ascii"
)

# Download ASCII data
response = requests.get(url)
ascii_data = response.text

# Convert ASCII (space-delimited) into DataFrame
df = pd.read_csv(StringIO(ascii_data), delim_whitespace=True)

# Rename columns for ML-friendly usage
df = df.rename(columns={
    "Flow_Speed": "speed",
    "Proton_Density": "density",
    "Bz_GSM": "bz",
    "Flow_Pressure": "pressure"
})

# Save to CSV
df.to_csv("omni_solarwind_2015_2025.csv", index=False)

print("CSV file saved as omni_solarwind_2015_2025.csv")
print(df.head())