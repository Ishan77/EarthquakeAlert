# Author: Ishan Subedi
# This program sends the earthquake message to defined people.

import sl4a
droid = sl4a.Android()
import urllib.request

# This fxn simply downloads the file and sends message to the defined relatives/people on the list.
def send_download(file_url,flag,phonelist):

    if flag:
        for phone in phonelist:
            droid.smsSend(phone,"There has been an earthquake stay alert")
            droid.ttsSpeak("Downloading file for earthquake safety")
            urllib.request.urlretrieve(file_url, filename="/sdcard/Download/Earthquake.pdf")
            droid.ttsSpeak("Download Completed")
            droid.ttsSpeak("There has been a severe earthquake.... Message sent to the defined People")
            droid.ttsSpeak("There has been a severe earthquake.... Message sent to the defined People")
