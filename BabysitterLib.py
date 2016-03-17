import subprocess, string, os, time
import xml.etree.ElementTree as xmlProcessor

def checkProcess(processname):
    tlcall = 'TASKLIST', '/FI', 'imagename eq %s' % processname
    # shell=True hides the shell window, stdout to PIPE enables
    # communicate() to get the tasklist command result
    tlproc = subprocess.Popen(tlcall, shell=True, stdout=subprocess.PIPE)
    # trimming it to the actual lines with information
    tlout = tlproc.communicate()[0].strip().split('\r\n')
    # if TASKLIST returns single line without processname: it's not running
    if len(tlout) > 1 and processname in tlout[-1]:
        return True
    else:
        return False
	
	
class log(object):
	# open or create log file
	def __init__(self, path="log.txt", name="Log"):
		self.logPath = path
		self.logName = name
		# check if file exists
		exists = os.path.isfile(self.logPath)
		# if log file dosn't exist, then create it and write the header line
		if not exists:
			with open(self.logPath, 'a') as f:
				f.write("---" + self.logName + " Log File---\n")
	
	# log any value to the log file
	def logWrite(self, log):
		self.datetimeStr = time.strftime("%m/%d/%y") + " " + time.strftime("%a") + " " + time.strftime("%H:%M")
		with open(self.logPath, 'a') as f:
			f.write(self.datetimeStr + " :  " + str(log) + "\n")
			
			