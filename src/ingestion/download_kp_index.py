import pandas as pd 
import requests 
from io import StringIO 

# ----------------------------
# NOAA Kp URL (Historical + Recent)
# ---------------------------- 
KP_URL = (
    "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
) 

OUTPUT_PATH = "data/raw/geomagnetic/kp_index.csv" 

def main():
    print("Downloading Kp index from NOAA..")
    response=  requests.get(KP_URL)
    response.raise_for_status() 
    
    data= response.json()
    df= pd.DataFrame(data)
    
     # Keep relevant columns
    df= df[["time_lag","kp_index"]]
    df.rename(columns={"time_tag": "timestamp_utc"}, inplace=True)
    
    df["timestamp_utc"]=pd.to_datetime(df["timestamp_utc"], utc=True) 
    df.to_csv(OUTPUT_PATH,index=False)
    
    print("✅ Kp index downloaded successfully")
    print(f"Saved to: {OUTPUT_PATH}")
    
if __name__ == "__main__":
    main()    