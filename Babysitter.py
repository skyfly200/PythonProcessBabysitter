# Import Babysitter Library
from BabysitterLib import *

# Load Process List From File
# this is the list of processes that should be running, folowed path to the process
list = xmlProcessor.parse("processes.xml")
processes = list.getroot().findall('process')

# Create a log object
startLog = log("restartLog.txt", "Software Restart Log")

# Check that all listed software is running
for process in processes:
	if not checkProcess(process.get('name')):
		print process.get('name')
		proc = subprocess.Popen(process.find('path').text)
		startLog.logWrite(process.get('name'))

