import requests
import json
import time
import os

def check_username(username, password):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Your Authorization token here",
    }
    data = {"username": username, "password": password}
    
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    
    return response.json()

def process_usernames(input_file_path, output_file_path, delay=60/24): # 24 requests per minute to avoid rate limit
    with open(input_file_path, 'r') as file:
        usernames = file.read().splitlines()

    with open(output_file_path, 'w') as outfile:
        for username in usernames:
            password = "" # Just empty so it doesn't change your name
            response = check_username(username, password)
            
            if 'errors' in response:
                if 'username' in response['errors']:
                    print(f"Username {username} is unavailable.")
                else:
                    print(f"Username {username} is free.")
                    outfile.write(username + "\n")
                    outfile.flush()
                    os.fsync(outfile.fileno())
            
            time.sleep(delay)

# Specify your file paths here
input_file_path = 'names.txt'
output_file_path = 'available.txt'
process_usernames(input_file_path, output_file_path)
