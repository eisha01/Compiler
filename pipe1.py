from subprocess import Popen, PIPE
import subprocess
args = ["input.py"]

process = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)

data = process.communicate()

print(data)


with subprocess.Popen(["compiler.xml"], stdout=subprocess.PIPE, shell=True) as process:
    output = process.stdout.read(40)
    print(output.decode())

s = subprocess.check_output(["echo", "welcome message"], shell=True)

print(s)