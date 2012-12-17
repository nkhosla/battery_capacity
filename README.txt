The goal of this project is very simple: make a python script and corresponding html document to allow people to upload output from the Android app CurrentWidget (found here:https://play.google.com/store/apps/details?id=com.manor.currentwidget&hl=en) to a server such that the returned information is an approximate battery capacity.  The capacity will be found from a numerical integration of current over time.  

This repository should at any given time really have only four files (unless it becomes much more complicated that originally planned).  Those files are:

*The readme.  This document
*The index.html.  Just a form for the file upload to get the CurrentWidget output to the python script
*The python script, a.k.a battery_capacity_estimator.py.  This script does the math.  
*a test CurrentWidget output csv found in ./test_files/current_widget_output.csv.  Using this as the test means that any math or logic errors should give inconsistent values (inconsistent with previous tests/a known value from another source of numerical integration) which is an easy built in red flag.

Thanks for looking at this.  If you have any comments or contributions, please feel free to make them known.  Keep in mind that this is my first jab at actually maintaining any type of code outside of a homework assignment and that I am not a ComSci student, so my coding or upkeep may get sloppy.

Nathan

