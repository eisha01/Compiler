import subprocess
import input


# Execute the "input" program and capture its output
input_popen = subprocess.Popen('input', stdout=subprocess.PIPE)
input_output = input_popen.stdout.read()
print(input_output)

# Prompt the user for additional data
user_data = input("Enter additional data: ")

# Print the additional data entered by the user
print("Additional data: ",user_data)