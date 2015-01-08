from json import dumps, loads
from urllib2 import urlopen, Request
import datetime

#Author: Senghor Louis Joseph
#        Harvey Mudd College '17
#        Engineering Student

#Total time working: 5hrs (mostly trying to figure out how to get a token)

# Research help: Google, Stack Overflow, Wikipedia, Python.org

receiveList =[]                     # List of the data extracted from each URL
info = {'token':'4U8eApHj2v'}       # My token in dictitonary form

myURLs = ['http://challenge.code2040.org/api/getstring',
          'http://challenge.code2040.org/api/haystack',
          'http://challenge.code2040.org/api/prefix',
          'http://challenge.code2040.org/api/time'] # All four POST URL 


for i in range(4):
    request = Request(myURLs[i], data=dumps(info))                  # Python info request
    receiveList.append(loads(urlopen(request).read())['result'])    # Places the dictionaries into this list, which will be accessed later; Major help from StackOverflow and Python.org
    
################################################# >>> Challenges

# Stage One ------------------------
def stringReverse():
    string = receiveList[0]                 # Set 'string' to whatever I received earlier
    r_String = string[::-1]                 # Reversed string
    print string, r_String                  
    return r_String                         # Final Value

# Stage Two ------------------------

def needleHaystack():
    needle = receiveList[1]['needle']       # Set 'needle' to whatever I received earlier
    haystack = receiveList[1]['haystack']   # Set 'haystack' to whatever I received earlier
    print "My Needle: " + needle            
    print "Needle Location: " + str(haystack.index(needle)) 
    return haystack.index(needle)           # Return the index number of the needle in the array

# Stage Three ----------------------

def prefix():
    prefix = receiveList[2]['prefix']       # Set 'needle' to whatever I received earlier
    array = receiveList[2]['array']         # Set 'needle' to whatever I received earlier

    print prefix
    print array
    
    prefLen = len(str(prefix))              # Find length of prefix
    resultList = []                         # Create an empty "Result List"
    for string in array:                    # For every string in the array...
        if (string[0:prefLen] != str(prefix)):  # ...if that string does not contain the prefix... 
            resultList.append(string)       # ...add it to the "Result List"
    print resultList
    return resultList                       # Return the results

# Stage Four -----------------------

def dates():
    datestamp = receiveList[3]['datestamp'] # Set 'datestamp' to whatever I received earlier
    interval = receiveList[3]['interval']   # Set 'interval' to whatever I received earlier

    print datestamp
    print interval

    time = datetime.datetime(int(datestamp[:4]),    # years
                             int(datestamp[5:7]),   # months
                             int(datestamp[8:10]),  # days
                             int(datestamp[11:13]), # hours
                             int(datestamp[14:16]), # minutes
                             int(datestamp[17:19]), # seconds
                             int(datestamp[20:23])) # UTC offset; major help from StackOverflow
    finalTime = time + datetime.timedelta(seconds=interval)
    return finalTime.isoformat()
    
#################################################

# Send it all away -----------------

myFunctions = [stringReverse(), needleHaystack(), prefix(),dates()]
mySendURLs = ['http://challenge.code2040.org/api/validatestring',
          'http://challenge.code2040.org/api/validateneedle',
          'http://challenge.code2040.org/api/validateprefix',
          'http://challenge.code2040.org/api/validatetime']
mySendKeys = ['string','needle','array','datestamp']

for i in range(4):
    send = {'token':'4U8eApHj2v', mySendKeys[i]:myFunctions[i]}
    res = Request(mySendURLs[i], data=dumps(send)) 
    final = loads(urlopen(res).read())['result']
    print final


#Grades:
send = {'token':'4U8eApHj2v'}
res = Request('http://challenge.code2040.org/api/status', data=dumps(send)) 
final = loads(urlopen(res).read())['result']
print final
