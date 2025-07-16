import subprocess
import os

def netstat():
    command = "netstat -an" if os.name == 'nt' else "ss -tunap"
    subprocess.run(command, shell=True)
