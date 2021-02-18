### THIS IS THE FILE THAT CALCULATES STATISTICAL MEASURES (MEAN & STANDARD DEVIATION) OF DATA ###
#Create a function capable of displaying all the relevant data from a Data object
from Code.classes_functions import Data

def display_data(Data_object):
    '''
    :param Data_object: Object of class data created from dataclasses
    :return: formatted string outputs
    This function takes in a data object and then displays all the mean and standard deviations
    of the data contained within the object
    '''
    print(
        "___________________________________________________________________________________\n"
        "Name of Monitor:{0} \n"
        "Type of data:{1} \n"
        "Channel of data: {2} \n".format(str(Data_object.name),str(Data_object.type),str(Data_object.channel))
    )
    if Data_object.type=="P":
        mean1CF1=Data_object.find_mean("PM1_CF1")
        sd1CF1 = Data_object.find_sd("PM1_CF1")
        mean25CF1 = Data_object.find_mean("PM25_CF1")
        sd25CF1 = Data_object.find_sd("PM25_CF1")
        mean25ATM = Data_object.find_mean("PM25_ATM")
        sd25ATM = Data_object.find_sd("PM25_ATM")
        mean10CF1 = Data_object.find_mean("PM10_CF1")
        sd10CF1 = Data_object.find_sd("PM10_CF1")

        print(
        "Mean PM 1.0 CF1 (ug/m^3): {0} \n"
        "Standard Deviation of PM 1.0 CF1 (ug/m^3): {1} \n"
        "\n"
        "Mean PM 2.5 CF1 (ug/m^3): {2} \n"
        "Standard Deviation of PM 2.5 CF1 (ug/m^3): {3} \n"
        "\n"
        "Mean PM 2.5 ATM (ug/m^3): {4} \n"
        "Standard Deviation of PM 2.5 ATM (ug/m^3): {5} \n"
        "\n"
        "Mean PM 10.0 CF1 (ug/m^3): {6} \n"
        "Standard Deviation of PM 10.0 CF1 (ug/m^3): {7} \n"
            .format(str(mean1CF1),str(sd1CF1),str(mean25CF1),str(sd25CF1),str(mean25ATM),str(sd25ATM),str(mean10CF1),str(sd10CF1))
        )
        if Data_object.channel =="A":
            Meantemp = Data_object.find_mean("Temperature")
            SDtemp = Data_object.find_sd("Temperature")
            Meanhumid = Data_object.find_mean("Humidity")
            SDhumid = Data_object.find_sd("Humidity")
            print("Mean Temperature (F): {0} \n"
            "Standard Deviation of Temperature (F): {1} \n"
            "\n"
            "Mean Humidity (%): {2} \n"
            "Standard Deviation of Humidity (%): {3} \n"
            "_______________________________________________________________________"
            .format(str(Meantemp),str(SDtemp),str(Meanhumid),str(SDhumid)))
        if Data_object.channel=="B":
            MeanPressure = Data_object.find_mean("Pressure")
            SDPressure = Data_object.find_sd("Pressure")
            print("Mean Pressure (HPa): {0} \n"
                  "Standard Deviation of Pressure (HPa): {1} \n"
                  "_______________________________________________________________________"
                  .format(str(MeanPressure), str(SDPressure)))
    elif Data_object.type=="S":
        mean1ATM = Data_object.find_mean("PM1_ATM")
        sd1ATM = Data_object.find_sd("PM1_ATM")
        mean10ATM = Data_object.find_mean("PM10_ATM")
        sd10ATM = Data_object.find_sd("PM10_ATM")
        mean03umdl = Data_object.find_mean("um_03_dl")
        sd03umdl = Data_object.find_sd("um_03_dl")
        mean05umdl = Data_object.find_mean("um_05_dl")
        sd05umdl = Data_object.find_sd("um_05_dl")
        mean1umdl = Data_object.find_mean("um_1_dl")
        sd1umdl = Data_object.find_sd("um_1_dl")
        mean25umdl = Data_object.find_mean("um_25_dl")
        sd25umdl = Data_object.find_sd("um_25_dl")
        mean5umdl = Data_object.find_mean("um_5_dl")
        sd5umdl = Data_object.find_sd("um_5_dl")
        mean10umdl = Data_object.find_mean("um_10_dl")
        sd10umdl = Data_object.find_sd("um_10_dl")

        print(
            "Mean PM 1.0 ATM (ug/m^3): {0} \n"
            "Standard Deviation of PM 1.0 ATM (ug/m^3): {1} \n"
            "\n"
            "Mean PM 10.0 ATM (ug/m^3): {2} \n"
            "Standard Deviation of PM 10.0 ATM (ug/m^3): {3} \n"
            "\n"
            "Mean Diameter of 0.3 um particles/decilitre of air (um/dl): {4} \n"
            "Standard Deviation of 0.3 um particles/decilitre of air (um/dl): {5} \n"
            "\n"
            "Mean Diameter of 0.5 um particles/decilitre of air (um/dl): {6} \n"
            "Standard Deviation of 0.5 um particles/decilitre of air (um/dl): {7} \n"
            "\n"
            "Mean Diameter of 1.0 um particles/decilitre of air (um/dl): {8} \n"
            "Standard Deviation of 1.0 um particles/decilitre of air (um/dl): {9} \n"
            "\n"
            "Mean Diameter of 2.5 um particles/decilitre of air (um/dl): {10} \n"
            "Standard Deviation of 2.5 um particles/decilitre of air (um/dl): {11} \n"
            "\n"
            "Mean Diameter of 5.0 um particles/decilitre of air (um/dl): {12} \n"
            "Standard Deviation of 5.0 um particles/decilitre of air (um/dl): {13} \n"
            "\n"
            "Mean Diameter of 10.0 um particles/decilitre of air (um/dl): {14} \n"
            "Standard Deviation of 10.0 um particles/decilitre of air (um/dl): {15} \n"
            "___________________________________________________________________________________"
            .format(
                str(mean1ATM),str(sd1ATM),str(mean10ATM),str(sd10ATM),
                str(mean03umdl),str(sd03umdl),str(mean05umdl),str(sd05umdl),str(mean1umdl),str(sd1umdl),
                str(mean25umdl),str(sd25umdl),str(mean5umdl),str(sd5umdl),str(mean10umdl), str(sd10umdl)
            )
        )

def display_some(Data_object, attribute):
    print(
        "Name of Monitor: {0} \n"
        "Type of Data: {1} \n"
        "Channel of Data: {2} \n"
        "Total number of observations: {3} \n"
        "Missing observations table: {4} \n"
        "------------------------------------------------\n"
        "Mean: {5} \n"
        "Minimum value: {6} \n"
        "Maximum value: {7} \n".format(Data_object.name,Data_object.type,
                                       Data_object.channel,str(Data_object.find_size(attribute)),
                                       str(Data_object.find_missing()), str(Data_object.find_mean(attribute)),
                                       str(Data_object.find_min(attribute)),str(Data_object.find_max(attribute)))
        )


#Create a function that finds all the data of a given list
def find_stats(Datalist):
    '''
    Takes in a list of data objects, and then calculates and displays the relevant stats below
     '''
    for object in Datalist:
        display_some(object)

##################### TESTING ZONE ###############################
'''
Input: 
data1 = Data("254 Wellington", "P", "A", "<insert path to corresponding CSV file on your computer>")

Output: display_data(data1)
==>
___________________________________________________________________________________
Name of Monitor:254 Wellington 
Type of data:P 
Channel of data: A 
Mean PM 1.0 CF1 (ug/m^3): 7.308162956052022 
Standard Deviation of PM 1.0 CF1 (ug/m^3): 6.89869340080349 
Mean PM 2.5 CF1 (ug/m^3): 11.725886729439592 
Standard Deviation of PM 2.5 CF1 (ug/m^3): 11.038220154237754 
Mean PM 2.5 ATM (ug/m^3): 11.463837596603248 
Standard Deviation of PM 2.5 ATM (ug/m^3): 9.95751685186844 
Mean PM 10.0 CF1 (ug/m^3): 12.482978455358229 
Standard Deviation of PM 10.0 CF1 (ug/m^3): 11.721194727025043 
Mean Temperature (F): 61.01373318635476 
Standard Deviation of Temperature (F): 19.879443082131804 
Mean Humidity (%): 50.4087242279911 
Standard Deviation of Humidity (%): 13.142845718920368 
_______________________________________________________________________
'''

#########################GENERAL INSTRUCTIONS ########################################
#############################################################################################
'''
CREATE Data objects from the given information: Monitor name, Primary or Secondary data ("P" or "S"),
Channel A or B ("A" or "B"), and link to given CSV file.

eg. 254 Wellington Primary Monitor A Data
data = Data("254 Wellington", "P", "A", "E:/Work Study AIr Pollution Research/254 Wellington/254 wellington st n (outside) (43.254591 -79.863272) Primary Real Time 06_26_2019 10_10_2020.csv")
'''
### ADD THE MONITOR NAME AND LINKS BELOW: create as many as needed ###
'''
data1 = Data("<insert monitor name>", "P", "A","<insert link to corresponding CSV file on your computer>")
data2 = Data ("<insert monitor name>", "S", "A","<insert link to corresponding CSV file on your computer>")
data3 = Data ("<insert monitor name>", "P", "B","<insert link to corresponding CSV file on your computer>")
data4 = Data ("<insert monitor name>", "S", "B","<insert link to corresponding CSV file on your computer>")
# ....(more data objects)...
'''

### LIST OF ALL THE Data objects: add more as needed ###
'''
Datalist = [data1,data2,data3,data4]
'''

### CONDUCT STATISTICAL ANALYSIS ON THE LIST ###
#Returns a display of the mean and standard deviations of all the relevant pollutant parameters'''
'''find_stats(Datalist)'''

