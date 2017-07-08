import socket
import pandas as pd

#read file and convert ip address to hostnames and hostnames to ip_address
def get_details(filename):

    hostname= []
    websitename=[]

    # Read excel file and also overwrite any NaN returned in columns
    sitenames = pd.read_excel(filename, na_values = 'NaN', keep_default_na = False)

    #First check any empty string is returned. If not empty string then go ahead and convert to ipaddress
    for address in sitenames['ipaddress']:
        if address != "":
            hostname.append(socket.gethostbyaddr(address)[0])

    #First check any empty string is returned. If not empty string then go ahead and convert to hostnames
    for sitename in sitenames['websitename']:
        if sitename != "":
            websitename.append(socket.gethostbyname(sitename))

    return hostname + websitename #return the combined list

websitenames = get_details("listofaddress.xlsx")

#print the result
for sitename in websitenames:
    print(sitename)






