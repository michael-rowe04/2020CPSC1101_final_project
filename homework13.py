import json
import requests
#pip3 install requests
strAPI = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2020-10-27&end_date=2020-10-27&api_key=gx1daXuj2m8vbtrVKtHALsIVu8U2yvBOWcbyjch8'
response = requests.get(strAPI)
json_data = json.loads(response.text)
print( json_data["links"]["prev"]) 

#retrieve name of asteroid
i=0

def print_names(i):
    print(json_data["near_earth_objects"]["2020-10-27"][i]["name"])

def print_diameter(i):
    print(json_data["near_earth_objects"]["2020-10-27"][i]["estimated_diameter"]["feet"]["estimated_diameter_min"])
    print(json_data["near_earth_objects"]["2020-10-27"][i]["estimated_diameter"]["feet"]["estimated_diameter_max"])
    

def print_distance(i):
    print(json_data["near_earth_objects"]["2020-10-27"][i]["close_approach_data"][0]["miss_distance"]["miles"])
    print('*****************************************************')   

while (i<json_data["element_count"]):
    print_names(i)
    print_diameter(i)
    print_distance(i)
    i = i + 1