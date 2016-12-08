#Author : Ishan Subedi

# These two functions take the JSON data and filter the required magnitude by the user and presents a simple list.

import sl4a
droid = sl4a.Android()



def filter_fxn(json_data,magnitudeThreshold):

    print(json_data["metadata"]["title"])
    print("------------------------------")
    print(json_data["metadata"]["count"])
    print("------------------------------")
    list1 = []
    list2 = []
    list3 = []
    interaction = False;
    for i in json_data["features"]:
        if i["properties"]["mag"] > magnitudeThreshold:

            magnitude = float(i["properties"]["mag"])
            actual_magnitude = "{0:.2f}".format(magnitude)
            list1.append(actual_magnitude)
            list2.append(i["properties"]["place"])
            interaction = True;


    for i in range(len(list1)):
        item = ("Magnitude: "+str(list1[i]) + " " +"Places: "+str(list2[i]))
        list3.append(item)

    droid_interface(list3)
    return interaction


# creates a GUI for the android phone
def droid_interface(list3):

    droid.dialogCreateAlert()
    droid.dialogSetItems(list3)
    droid.dialogShow()