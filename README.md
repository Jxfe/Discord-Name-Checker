# Discord Username Availability Checker

This is a Python script that checks a list of usernames for their availability on Discord. The script reads from a file containing the usernames (one per line), checks the availability of each username using Discord's API, and outputs the status of each username.

## Requirements

- Python 3
- `requests` library 

To install the `requests` library, run the following command:

```shell
pip install requests
```

## Usage
Update the Authorization token in the check_username function in main.py with your actual token.
Add the usernames you want to check to the names.txt file, with one username per line.
Run the script with the command python Discord.py.
The script will check each 25 usernames every minute to avoid rate limit.
