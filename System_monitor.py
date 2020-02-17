import psutil
import os
import requests
import json
web_hook_url = 'https://hooks.slack.com/services/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'
slack_msg_memory = {'text':'System is not safe, Used Memoery is more than 80%'}
slack_msg_disk = {'text':'System is not safe, Disk usage is more than 90%'}
slack_msg_cpu = {'text':'System is not safe, cpu usage is more than 80%'}

hostname = "8.8.8.8"   # IP for google.com

Memory_Usage=psutil.virtual_memory()
Cpu_percent=psutil.cpu_times_percent(interval=1)
Load=psutil.getloadavg()
Disk_Usage=psutil.disk_usage('/')

print("Memory Usage of system is: " + str(Memory_Usage))
print("CPU percent of system is: " + str(Cpu_percent))
print("Load on system is: " + str(Load))
print("Disk Usage of system is: " + str(Disk_Usage))
response = os.system("ping -c 5 " + hostname)

if Memory_Usage.percent >= 80:
	print("This is not safe, Used Memoery is more than 80%")
	requests.post(web_hook_url,data=json.dumps(slack_msg_memory))

if Disk_Usage.percent >= 90:
	print("This is not safe, Disk usage is more than 90%")
	requests.post(web_hook_url,data=json.dumps(slack_msg_disk))
if Cpu_percent.idle <= 20:
	print("This is not safe, cpu usage is more than 80%")
	requests.post(web_hook_url,data=json.dumps(slack_msg_cpu))
	
