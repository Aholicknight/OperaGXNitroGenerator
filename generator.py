import requests
import time
import ctypes
import os
import uuid
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Ask how many requests/links to make
print(f"{Fore.MAGENTA}Discord Nitro Generator{Style.RESET_ALL} by {Fore.RED}AholicKnight{Style.RESET_ALL}")
num_requests = int(input("How many requests/links would you like to make? "))

# URL to send POST requests to
url = "https://api.discord.gx.games/v1/direct-fulfillment"

# Counter for successful requests
successful_requests = 0

# Animation characters
animation_chars = ['/', '-', '\\', '|']

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# Create the generatedcodes.txt file if it doesn't exist
if not os.path.exists("generatedcodes.txt"):
    open("generatedcodes.txt", "w").close()

# Open the file to write the responses
with open("generatedcodes.txt", "w") as file:
    for i in range(num_requests):
        # Generate a new UUID for each request
        data = {"partnerUserId":str(uuid.uuid4())}

        # Send the POST request
        response = requests.post(url, json=data)

        if response.status_code == 200:
            token = response.json().get('token')
            if token:
                successful_requests += 1
                link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
                file.write(f"{link}\n")
        elif response.status_code == 429:
            print(f"{Fore.YELLOW}You are being rate-limited!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Request failed : {response.status_code}{Style.RESET_ALL}")

        # Print the animation and the number of successful requests to the console
        print(f"\rGenerating codes {animation_chars[i % len(animation_chars)]}.....({Fore.GREEN}{successful_requests}{Style.RESET_ALL}) out of {num_requests}", end="")

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# Print the final message
print(f"Generated {Fore.GREEN}{successful_requests}{Style.RESET_ALL} successfully!")
input("Press any key to exit")