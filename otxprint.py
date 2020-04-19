import re
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
otx = OTXv2("39cf879fe132e36e50547ea5d9fe5911c3ce099d4ef7680a42c29cf84153a740")
otxlist = ["5e9a305bf4a514345e851c22","5e9b81b20fa89499c3492c5b","5e9b89d2dd401d48efca8815","5e9b9360c9f1ecea115ecc22","5e9b9363705f075c45ca8815","5e9b936449addd4c29492c5b","5e9b9362e91d1f3f53e2743b","5e9b93ce1db0f133f152f14e"]

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
    
def getIndicatorsfromList():
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
            
    
def printListToFile(filename):
    fo = open(filename,"a+")
    for indicator in indicators:
        fo.write(indicator["indicator"])


if __name__ == "__main__":
    import sys
    getIndicatorsfromList()
    #printListToFile(str(sys.argv[1]))
    
