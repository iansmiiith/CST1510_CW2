import requests
import csv
import os
url = "https://randomuser.me/api/? results=10"
print("Fetching data from API...")
response = requests.get(url)
data = response.json()
os.makedirs("DATA", exist_ok=True)
file_path = "DATA/raw.csv"
results = data['results']
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["First Name", "Last Name", "Email", "Country"])
    for user in results:
        writer.writerow([
            user['name']['first'],
            user['name']['last'],
            user['email'],
            user['location']['country']
        ])
print(f"Success! Data saved to {file_path}")