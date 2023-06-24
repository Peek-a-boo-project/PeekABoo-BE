import requests
import json

def get_group_feed_data(group_id, access_token):
    api_version = "v17.0" #update with the desired API version
    url = f"https://graph.facebook.com/{api_version}/{group_id}/feed"

    params = {"access_token": access_token, "fields":"place,message,created_time,full_picture, permalink_url"}

    response = requests.get(url, params=params)
    data = response.json()

    if "data" in data:
        return data["data"]
    else:
        print("Error retrieving data from Facebook API")
        print(data)
        return []
