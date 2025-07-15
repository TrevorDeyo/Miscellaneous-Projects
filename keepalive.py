import time
import subprocess
import psutil

# Name of the .exe to check
process_name = "FactoryServer.exe"
# Full path of the executable
exe_path = "C:\\steamcmd\\steamapps\\common\\SatisfactoryDedicatedServer\\FactoryServer.exe"

def is_process_running(process_name):
    # Check if the process is running
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

def start_process(exe_path):
    # Start the executable
    subprocess.Popen([exe_path])

print("Starting keepalive...")
counter = 0
while True:
    if not is_process_running(process_name):
        print(f"{process_name} not running, starting it now...")
        start_process(exe_path)
        counter += 1
        print(counter)

    # Wait for a minute before checking again
    time.sleep(30)
