import requests
import json
import time

def check_username(username, password):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Your Authorization token here",
    }
    data = {"username": username, "password": password}
    
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    
    return response.json()

def process_usernames(file_path, delay=60/24): # 24 requests per minute so avoid rate limit
    with open(file_path, 'r') as file:
        usernames = file.read().splitlines()

    for username in usernames:
        password = "" # Just empty so it doesnt change your name
        response = check_username(username, password)
        
        if 'errors' in response:
            if 'username' in response['errors']:
                print(f"Username {username} is unavailable.")
            else:
                print(f"Username {username} is free.")
        
        time.sleep(delay)

# Specify your file path here
file_path = 'names.txt'
process_usernames(file_path)
