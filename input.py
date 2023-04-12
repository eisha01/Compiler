import subprocess
import datetime
import os

# Get the current logged-in user
username = subprocess.check_output("whoami").strip().decode()

# Get the current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Print the welcome message
print("Welcome " + username + "! The current date and time is " + current_time)

print(os.getlogin())