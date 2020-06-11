# simplespeedtest
This repo contains software to test your internet connection speed.

Currently it consists of two files:

- simplespeedtest.py: the actual program to run the simplespeedtest
- simplespeedtest.ini: the input parameters for simplespeedtest.py. Currently it has three parameters:
    - outputFile: the name of the file where output goes. Typically this will be a CSV file that you can pull into spreadsheet software to analyze
    - sleepTime: the number of seconds before each test
    - silentMode: if you set this to False, it will print stats on the console. If you set it to anything else, the program will not write to the console. The program will always write to the outputFile thought.

If you enter: python simplespeedtest.py, it will read the simplespeedtest.ini and then continue running until you cause the program to end. 

IMPORTANT: If you get SSL related errors, enter the following from the command line and then rerun the Python script: export PYTHONHTTPSVERIFY=0
