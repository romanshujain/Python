import psutil

Memory_Usage=psutil.virtual_memory()
Cpu_persent=psutil.cpu_times_percent(interval=1)
Load=psutil.getloadavg()
Disk_Usage=psutil.disk_usage('/')

print("Memory Usage of system is: " + str(Memory_Usage))
print("CPU percent of system is: " + str(Cpu_persent))
print("Load on system is: " + str(Load))
print("Disk Usage of system is: " + str(Disk_Usage))

if Memory_Usage.percent >= 80:
	print("This is not safe, Used Memoery is more than 80%")

if Disk_Usage.percent >= 90:
	print("This is not safe, Disk usage is more than 90%")
























#Memory=psutil.virtual_memory()
#Cpu=


#with open("/proc/loadavg", "r") as f:
 #   print("Average Load: " + f.read().strip())



#print("Memory Info: ")
#with open("/proc/meminfo", "r") as f:
 #   lines = f.readlines()

#print("     " + lines[0].strip())
#print("     " + lines[1].strip())


# let's print CPU information
#print("="*40, "CPU Info", "="*40)
# number of cores
#print("Physical cores:", psutil.cpu_count(logical=False))
#print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
#cpufreq = psutil.cpu_freq()
#print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
#print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
#print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
#print("CPU Usage Per Core:")
#for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
#    print(f"Core {i}: {percentage}%")
#print(f"Total CPU Usage: {psutil.cpu_percent()}%")
