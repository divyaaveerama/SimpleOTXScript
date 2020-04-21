import re
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
otx = OTXv2("") #put your A.P.I key in there
otxlist = ["",""] #put the pulse IDs in here
#Create lists for each type of IOC
IPs = []
URLs = []
Senders = []
MD5s = []
SHAs = []

#Create regular expressions to pick out specific types of IOCs from the list
URL = re.compile(r'^([a-zA-Z0-9\-\.]+\.[a-zA-Z]+)$')
MD5 = re.compile(r'^([a-z0-9]{32})$')
SHA256 = re.compile(r'^([a-z0-9]{64})$')
IP = re.compile(r'^([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)$')

# Get all the indicators associated with a pulse
def getIndicators(pulse_id):
    indicators = otx.get_pulse_indicators(pulse_id)
    for indicator in indicators:
        print(indicator["indicator"])

        
def getIndicatorsfromList(): #use this if you have multiple pulses to scrape
    for pulse_id in otxlist:
    
        indicators = otx.get_pulse_indicators(pulse_id)
        
        for indicator in indicators:
            #check to see if the IOC matches the format of the IOC and if they do, will be appended to the appropriate list
                                                        
            if URL.match(indicator["indicator"]) and indicator["indicator"] not in URLs: 
                URLs.append(indicator["indicator"])
            elif IP.match(indicator["indicator"]):
                IPs.append(indicator["indicator"])
            elif SHA256.match(indicator["indicator"]) and indicator["indicator"] not in SHAs: #Check if it matches the format of an SHA256 hash and is not a duplicate
                SHAs.append(indicator["indicator"])
            elif MD5.match(indicator["indicator"]) and indicator["indicator"] not in MD5s: #Check if it matches the format of an MD5 Hash and is not a duplicate
                MD5s.append(indicator["indicator"])
            
    print("IPs:")
    for ip in IPs:
        print(ip)
        
    print("\n")
    print("URLs:")    
    for url in URLs:
        print(url)
        
    print("\n")
    print("SHA256s:")
    for sha in SHAs:
        print(sha)
        
    print("\n")
    print("MD5s:")    
    for md5 in MD5s:
        print(md5)
        
    print("\n")    
            
    
def printListToFile(filename): #ignore this for now
    fo = open(filename,"a+")
    for indicator in indicators:
        fo.write(indicator["indicator"])


if __name__ == "__main__":
    import sys
    getIndicatorsfromList()
    #getIndicators(str(sys.argv[1])) #use this if you only have 1 pulse to scrape
    
