import psutil
import datetime

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)

# Get RAM usage
memory = psutil.virtual_memory()
ram_usage = memory.percent

# Get Disk usage
disk = psutil.disk_usage('/')
disk_usage = disk.percent

# Get system uptime
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
current_time = datetime.datetime.now()
uptime = current_time - boot_time

# Create log message
log_message = f"""
System Health Report
Time: {current_time}

CPU Usage: {cpu_usage}%
RAM Usage: {ram_usage}%
Disk Usage: {disk_usage}%
System Uptime: {uptime}

----------------------------
"""

# Save log to file
with open("system_log.txt", "a") as file:
    file.write(log_message)

print("System health check completed. Log saved.")