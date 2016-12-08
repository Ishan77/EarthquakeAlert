# Author: Ishan Subedi

from Interface import *
from JsonData import *
from Message import *

# set the magnitude of the earthquake here. I have set to 4 as a  default.
magnitudeThreshold = 4

#Set the phoneList here. Standard charges apply as per your phone carrier.
#Also the elements in  phonelist has to be a string.
phonelist=[]

#set the url of the Json data here.
url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

#Url of the file to be downloaded in case of an emergency, this is a redcross file.
file_url = "http://www.redcross.org/images/MEDIA_CustomProductCatalog/m4240216_Earthquake.pdf"

# Invoke the function
flag = filter_fxn(status_link(url),magnitudeThreshold)
send_download(file_url,flag,phonelist)
