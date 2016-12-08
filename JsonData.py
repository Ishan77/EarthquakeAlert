# Author: Ishan Subedi

""" The purpose of this function is to decode the JSON data from the USGS website."""

import urllib.request
import json


# This function takes in the USGS link and returns the JSON data in a dictionary form.
def status_link(link):
    webOpen = urllib.request.urlopen(link)
    success = (webOpen.getcode())
    count = 0
    while success != 200 and count > 5:
        print("")
        print("Server not Established", count, "trial")
        count += 1
    print("")
    print("Server Established....Cracking The JSON")

    data = (webOpen.read())
    json_data = json.loads(data.decode())
    return json_data
