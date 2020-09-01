#!/usr/bin/python
# Title: Finding area code in Pi
# File: piThing.py
# External Files: N/A
# Author: Robert Kaufman
# Email: rlkxkd@umsystem.edu
# CS4500-001
# 27Aug2020
# Resources: The pi_spigot function was found at https://programmingpraxis.com/2009/02/20/the-digits-of-pi/

def pi_spigot():
    """
    This function yields a single digit of pi at a time
    """
    (q, r, t, k, n, l) = (1, 0, 1, 1, 3, 3) # variables required to calculate successive pi digits
    while True:
        if 4*q+r-t < n*t:
            yield n
            (q, r, t, k, n, l) = (10*q, 10*(r-n*t), t, k, (10*(3*q+r))//t-10*n, l)
        else:
             (q, r, t, k, n, l) = (q*k, (2*q+r)*l, t*l, k+1, (q*(7*k+2)+r*l)//(t*l), l+2)
 
 
def findZipCodeInPi(n, zipCode):
    """
    This function will print the index of the zipCode if it is found in pi
    """
    compStr = [] # Used to store a running 5 digits of pi to compare 'zipCode' against
    digit = pi_spigot() # For better understandability. Makes it obvious what next(digit) returns
    index = 0 # stores current index. Just used for printing out the index when the zip code is found
    # Below loop with run until zipCode matches the comparison list. 
    while n > 0:
        if (compStr == zipCode):
            print("Found your zipcode at index " + str(index-4))
            break
        if len(compStr) == 5:
            compStr.pop(0) # removs the 1st element of the list. This ensures compStr is always 5 digits long
        compStr.append(next(digit))
        n -= 1
        index += 1
    if (n == 0):
        print("Could not locate that zip code in the first %d digits of pi" % (n + index))

def isValid(x):
    """
    This function makes sure the input is 5 characters long and only contains digits
    """
    if len(x) != 5 or not x.isdigit():
        return False
    return True

rawData = input('Enter a 5 digit zip code: ')
# This while loop checks the validity of the input and keeps reprompting until it is correctly formatted
while not isValid(rawData):
    rawData = input('Input error. Enter exactly 5 consecutive numeric characters: ')
zipCode = []
# This for loop stores the input string into a list of integers for the find function
for i in rawData:
    zipCode.append(int(i))
    
findZipCodeInPi(1000000, zipCode)
