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
# Set your group ID and access token
group_id = "{your group id}}"
access_token = "{your access token}"

# Call the function to get the group's feed data
group_feed_data = get_group_feed_data(group_id, access_token)

# json 객체로 변환 + utf-8로 인코딩
json_data = json.dumps(group_feed_data, indent=4, ensure_ascii=False).encode("utf-8")

# json 파일로 저장
with open("results.json", "wb") as f:
    f.write(json_data)
