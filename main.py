import time
import psutil, datetime
from datetime import timedelta

# System Info
print("\n")
print("*" * 10, "System Info", "*" * 10)
# Device running date
print("Device Running Since:", datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")) 
# Device uptime
Device_Uptime = timedelta(seconds=time.time()-psutil.boot_time())
print(f"Device Uptime: {Device_Uptime}")
# CPU Time
CPU_Time = timedelta(seconds=psutil.cpu_times().system+psutil.cpu_times().user)
print(f"Time on CPU: {CPU_Time}")
# Disk Free
Disk_Free = psutil.disk_usage('/')
print(f"Disk Free: {Disk_Free.free/(1024**3):,.2f} GiB") 
users = psutil.users()
# Prints current user
for user in users:
    print("Current User:", user.name)


# Process Info
print("\n", "*" * 10, "Process Info", "*" * 10)
CPU_Frequency = psutil.cpu_freq()
print(f"Current Frequency: {CPU_Frequency.current:.2f}Mhz")
CPU_Cores = psutil.cpu_count()
# CPU Cores
print(f"Number of cores in system: {CPU_Cores}") 
Memory_Available = psutil.virtual_memory()
# Memory Available
print(f"Memory Available: {Memory_Available.available/(1024**3):,.3f} GiB") # Memory Available
print("\n")


def display_usage(cpu_usage, mem_usage, disk_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars)) # CPU Bar
    
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars)) # Memory Bar

    disk_percent = (disk_usage / 100.0)
    disk_bar = '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars)) # Disk Bar

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ", end="")
    print(f"Mem Usage: |{mem_bar}| {mem_usage:.2f}% ", end="")
    print(f"Disk Usage: |{disk_bar}| {disk_usage:.2f}% ", end="\r")

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.disk_usage('/').percent, 30)
    time.sleep(0.5)
