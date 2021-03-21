#Use this file to get the access token.
import requests.auth
client_auth = requests.auth.HTTPBasicAuth('<Add client ID here>', '<Add client secret here>')
post_data = {"grant_type": "password", "username": "<Add Reddit username here>", "password": "<Add Reddit password here>"}
headers = {"User-Agent": "<Add name of user agent here>"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
print(response.json())
