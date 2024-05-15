#Created By ARXU
import requests
import getpass
from termcolor import colored

def find_admin_panel(target_url, username, password):
    # Load the admin dorks from a text file
    with open('admin_dorks.txt', 'r') as f:
        admin_dorks = [line.strip() for line in f]

    # Initialize the results dictionary
    results = {
        'Target URL': target_url,
        'Admin Panels Found': [],
        'Status Codes': {}
    }

    # Print your logo with colors
    print(colored(" __    __   _______  __       __        ______", 'green'))
    print(colored("|  |  |  | |   ____||  |     |  |      /  __  \ ", 'green'))
    print(colored("|  |__|  | |  |__   |  |     |  |     |  |  |  | ", 'green'))
    print(colored("|   __   | |   __|  |  |     |  |     |  |  |  | ", 'green'))
    print(colored("|  |  |  | |  |____ |  .|  --.|  --'  | ", 'green'))
    print(colored("||  || |___| \/ ", 'green'))
    print(colored("\n ARXU'S BAD MAGIC \n", 'red'))
    print(colored("Telegram : https://t.me/A0R3A", 'blue'))

    # Prompt for username and password
    username_input = input("Enter your username: ")
    password_input = getpass.getpass("Enter your password: ")

    # Check if username and password are correct
    if username_input == 'arxu' and password_input == 'hell':
        # Iterate through each admin dork
        for dork in admin_dorks:
            # Construct the full URL
            full_url = target_url.strip('/') + dork

            try:
                # Send a HEAD request to the target URL with authentication
                response = requests.head(full_url, auth=(username, password))
                status_code = response.status_code
                results['Status Codes'][full_url] = status_code

                # Check for all standard HTTP status codes
                if 100 <= status_code < 200:
                    color = 'green'
                elif 200 <= status_code < 300:
                    color = 'blue'
                elif 300 <= status_code < 400:
                    color = 'yellow'
                elif 400 <= status_code < 500:
                    color = 'red'
                elif 500 <= status_code < 600:
                    color = 'magenta'
                else:
                    color = 'white'

                status_code_message = colored(f"Status Code: {status_code}", color)
                results['Status Codes'][full_url] = status_code_message

                if status_code in [200, 400, 404]:
                    results['Admin Panels Found'].append(full_url)

            except requests.exceptions.RequestException as e:
                print(colored(f"\nERROR: {e}", 'red'))
                print("Ahhh, the dark magic of the interwebs thwarts our progress!\n")
                break

    else:
        print(colored("Incorrect username or password. Access denied.", 'red'))
        return

    return results

# Input target URL from the user
target_url = input("Enter the target URL (including http(s)://): ")

# Prompt for username and password
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# Start the scanning process
print(colored("Scanning for admin panels... ", 'blue'))
results = find_admin_panel(target_url, username, password)

# Print the results
if 'Admin Panels Found' in results:
    print("\nScan Results:")
    print("Target URL:", results['Target URL'])
    print("Admin Panels Found:", results['Admin Panels Found'])
    print("Status Codes:", results['Status Codes'])
else:
    print(colored("No admin panels found.", 'red'))
