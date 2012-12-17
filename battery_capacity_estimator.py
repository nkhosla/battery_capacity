#!/usr/bin/python

#---------------------------------------------
#=============================================
#---------------------------------------------
#imports

import time as tm
#import numpy as np
from numpy import trapz
import os
import cgi, cgitb

cgitb.enable()

#---------------------------------------------
#=============================================
#---------------------------------------------
#seconds stuff

def getBaseSeconds(csv_time_input):
	#I know that the csv time is input as YYYY/MM/DD HH:MM:SS
	#so I use that to translate it to seconds (technically sec since
	#the epoch (aka unix epic time))
	base=int(tm.mktime(tm.strptime(csv_time_input, '%Y/%m/%d %H:%M:%S')))
	return base
	
def getSeconds(csv_time, baseTime):
	#I know that the csv time is input as YYYY/MM/DD HH:MM:SS
	#so I use that to translate it to seconds (technically sec since
	#the epoch (aka unix epic time))
	
	#Then, I can take the baseTime argument and just subtract 
	#it from the rawTime
	#Thus, I do not have to store huge numbers for no good reason
	rawTime=int(tm.mktime(tm.strptime(csv_time, '%Y/%m/%d %H:%M:%S')))
	processedTime=rawTime-baseTime
	return processedTime

#---------------------------------------------
#=============================================
#---------------------------------------------
#the main part of the script

form = cgi.FieldStorage()

#The variables
dataArray=[]
current = []
time = []
#percent = []



#get the fileitem
fileitem=form['userfile']
if fileitem.file:
    #yay...we got a file
    for line in fileitem.file:
		#read the data from the file
		dataHolder=line.split(',')
	
		#if a row has a length different than 3, something went wrong and the
		#row cannot be analyzed, so its data point is thrown out
		if len(dataHolder) == 3:
			dataArray.append(dataHolder)

		#make the arrays for time, current, and percent		
		#read the data into the above arrays, processing it as necessary
		#ex: stripping mA from the current so that it is just numbers
		#and defining a basetime such that point zero is at t=0
		#instead of the UET value

baseTimeHolder = dataArray[0][0]
baseTime=getBaseSeconds(baseTimeHolder)

for entry in dataArray:
			
	timeHolder=entry[0]
	currentHolder = entry[1]
#	percentHolder=entry[2]
			
#	percent.append(int(percentHolder.strip('% \nr')))
	current.append(int(currentHolder.strip('mA \nr')))
	time.append((getSeconds(timeHolder.strip(),baseTime)))

capacity_mAs= trapz(current, x=time)
capacity_mAh=-capacity_mAs/(60**2)

totalTime=time[len(time)-1]
  
    
#---------------------------------------------
#=============================================
#---------------------------------------------
#Output
    
    
    
print """\
Content-Type: text/html\n
<html><body>
<p>Your battery capacity is approximately: %s mAh</p>
<p>The data in your file spanned %s seconds = %s minutes</p>
</body></html>
""" % (capacity_mAh,totalTime, totalTime/60,)

