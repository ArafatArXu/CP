
import requests
import getpass

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

    # Print your logo
    print(" __    __   _______  __       __        ______")
    print("|  |  |  | |   ____||  |     |  |      /  __  \ ")
    print("|  |__|  | |  |__   |  |     |  |     |  |  |  | ")
    print("|   __   | |   __|  |  |     |  |     |  |  |  | ")
    print("|  |  |  | |  |____ |  .|  --.|  --'  | ")
    print("||  || |___| \/ ")
    print("\n ARXU'S BAD MAGIC \n")

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
                if 100 <= status_code < 200 or \
                    200 <= status_code < 300 or \
                    300 <= status_code < 400 or \
                    400 <= status_code < 500 or \
                    500 <= status_code < 600:
                    results['Admin Panels Found'].append(full_url)

            except requests.exceptions.RequestException as e:
                print(f"\nERROR: {e}")
                print("Ahhh, the dark magic of the interwebs thwarts our progress!\n")
                break

    else:
        print("Incorrect username or password. Access denied.")
        return

    return results

# Input target URL from the user
target_url = input("Enter the target URL (including http(s)://): ")

# Prompt for username and password
username = input("Enter your username:")
password = getpass.getpass("Enter your password:")

# Start the scanning process
print("Scanning for admin panels... ")
results = find_admin_panel(target_url, username, password)

# Print the results
if 'Admin Panels Found' in results:
    print("\nScan Results:")
    print("Target URL:", results['Target URL'])
    print("Admin Panels Found:", results['Admin Panels Found'])
    print("Status Codes:", results['Status Codes'])
else:
    print("No admin panels found.")