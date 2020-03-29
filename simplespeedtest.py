#############################################################################
#
# simplespeedtest.py                                 
#
# Description:
#  
#	This program continually measures the upload, download and 
# ping speeds of your internet connection, and then writes that information
# in CSV format to an output file.
#
# History:
#
#       2020.03.28	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python implespeedtest.py <my.ini>
#       the my.ini parameter is optional. If you don't specify it, this
#	program will default to assuming my.ini = simplespeedtest.ini
#
#############################################################################

import ConfigParser         # needed to process the input file
import sys		    # needed to process input parameters
import speedtest            # needed for running the actual speed test 
import time                 # needed for sleeping
from datetime import datetime # needed for date and time stamp


# Process the input parameters.
if len(sys.argv) == 2:
	iniFile = sys.argv[1]
	inputParm = "NotGiven"

elif len(sys.argv) == 3:
	iniFile = sys.argv[1]
	inputParm = int(sys.argv[2])

else:
	iniFile = "simplespeedtest.ini"
        print "I am assuming you are going with an input file of ", iniFile

# The format of speedtest.ini is like this (minus the #). Note, no quote around the string
# outputFile is assumed to be a CSV file
# sleepTime is in seconds (e.g. 300 seconds is 5 minutes). Don't make it too short
# This program tests if silentMode is False. Any other value will make silentMode
# equal true.
#
# [DEFAULT]
# outputFile = simplespeedtest.csv
# sleepTime = 300
# silentMode = False

# Parse the inifile. If there is an error, then exit
try:
   config = ConfigParser.ConfigParser()
   config.read(iniFile)
except:
   print "Error reading the inifile ", iniFile
   sys.exit()

# Assign iniFile values to program variables. If there an error, then exit
try:
   outputFile = config.get('DEFAULT', 'outputFile')
   sleepTime =  float(config.get('DEFAULT', 'sleepTime'))
   silentMode = config.get('DEFAULT', 'silentMode')
except:
   print "Invalid values in the ", iniFile, " See the code comments for help."
   sys.exit()


# Open the outputFile and then loop forever.

f = open(outputFile, "a")

print "This program will continue until you stop it. (e.g. enter: ctrl+c)"

while True:

  # Get the download speed, the upload speed, and the ping speed. Convert them to
  # from bps to mbps and turn them into strings.
  
  st = speedtest.Speedtest() 

  downloadbps = st.download() 
  downloadmbps = str(downloadbps / (1024 * 1024))

  uploadbps = st.upload() 
  uploadmbps = str(uploadbps / (1024 * 1024))

  servernames =[] 
  st.get_servers(servernames) 
  pingdata = str(st.results.ping)
  
  timeStamp = str(datetime.now())

  if silentMode == "False":  
     print timeStamp + ' download ' + downloadmbps + ' mbps upload ' + uploadmbps + ' ping ' + pingdata + ' ms'
     
  # Write to a file

  outputRecord = timeStamp + "," +  downloadmbps +  "," + uploadmbps + "," + pingdata + "\n"
  f.write(outputRecord)

  # Sleep and then check the speed again
  time.sleep(sleepTime)

# End of program. Close the output file
f.close()

