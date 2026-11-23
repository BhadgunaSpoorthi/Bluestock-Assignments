import requests
import pandas as pd
url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)
print("Status Code:", response.status_code)
json_data = response.json()
print(json_data)
df = pd.DataFrame(json_data["data"])
df.to_csv("data/nav_data.csv", index=False)

print("CSV Created Successfully")