import csv
import numpy as np
import pandas as pd

class Data:
    def __init__(self,name,type,channel,link):
        '''
        :param name: Name of monitor (String)
        :param type: Primary or Secondary (String)
        :param channel: A or B
        :param link: Link to CSV file
        Creates a Data object based on the inputs of basic info
        '''
        self.name=name #string attribute
        self.type=type #string attribute
        self.channel=channel #string attribute
        self.link=link #string attribute
        self.all_data=pd.read_csv(link) #DataFrame attribute

        #Assign all the data attributes to each column indexed from the DataFrame --> turn into Numpy arrays
        self.created_at=self.all_data["created_at"].to_numpy()
        self.entry_id = self.all_data["entry_id"].to_numpy()

        if type=="P":
            self.PM1_CF1 = self.all_data["PM1.0_CF1_ug/m3"].to_numpy(dtype=float)
            self.PM25_CF1 = self.all_data["PM2.5_CF1_ug/m3"].to_numpy(dtype=float)
            self.PM10_CF1 = self.all_data["PM10.0_CF1_ug/m3"].to_numpy(dtype=float)
            self.PM25_ATM = self.all_data["PM2.5_ATM_ug/m3"].to_numpy(dtype=float)
            self.UptimeMinutes = self.all_data["UptimeMinutes"].to_numpy(dtype=int)
            if channel=="A":
                self.RSSI_dbm = self.all_data["RSSI_dbm"].to_numpy(dtype=int)
                self.Temperature = self.all_data["Temperature_F"].to_numpy(dtype=int)
                self.Humidity =  self.all_data["Humidity_%"].to_numpy(dtype=int)
            elif channel=="B":
                self.ADC=self.all_data["ADC"].to_numpy(dtype=int)
                self.Pressure=self.all_data["Pressure_hpa"].to_numpy(dtype=int)
        elif type=="S":
            self.PM1_ATM
            self.PM10_ATM
            self.um_03_dl = self.all_data[">=0.3um/dl"].to_numpy(dtype=float)
            self.um_05_dl = self.all_data[">=0.5um/dl"].to_numpy(dtype=float)
            self.um_1_dl = self.all_data[">=1.0um/dl"].to_numpy(dtype=float)
            self.um_25_dl = self.all_data[">=2.5um/dl"].to_numpy(dtype=float)
            self.um_5_dl = self.all_data[">=5.0um/dl"].to_numpy(dtype=float)
            self.um_10_dl = self.all_data[">=10.0um/dl"].to_numpy(dtype=float)

    def find_mean(self, attribute):
        ''' Takes in an attribute and finds the mean for the given attribute
        :param parameter: name of pollutant parameter (string)
        output: float
        '''
        array = self.__getattribute__(attribute)
        mean = np.mean(array)
        return mean
    def find_median(self,attribute):
        '''(string) --> (float)
            Takes in an attribute as a string. Finds corresponding array as an attribute of the Data object.
            calculates the median from all the elements inside it'''
        array = self.__getattribute__(attribute)
        median = np.median(array)
        return median

    def find_sd(self,attribute):
        '''
        :param attribute: string name of the Data Object attribute
        :return: float
        Takes in an attribute as a string. Finds corresponding array as an attribute of the Data object
        Calculates the standard deviation of all the elements inside it.
        '''
        array=self.__getattribute__(attribute)
        sd = np.std(array)
        return sd

    def find_var(array):
        '''
       :param attribute: string name of the Data Object attribute
        :return: float
        Takes in an attribute as a string. Finds corresponding array as an attribute of the Data object
        Calculates the variance of all the elements inside it.
        '''
        array = self.__getattribute__(attribute)
        var = np.var(array)
        return var
#Create a function capable of displaying all the relevant data from a Data object
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
#Create a function that finds all the data of a given list
def find_stats(Datalist):
    '''
    Takes in a list of data objects, and then calculates and displays the relevant stats below
     '''
    for object in Datalist:
        display_data(object)



###########Testing code###################
data1 = Data("254 Wellington", "P", "A", "E:/Work Study AIr Pollution Research/254 Wellington/254 wellington st n (outside) (43.254591 -79.863272) Primary Real Time 06_26_2019 10_10_2020.csv")
datalist = [data1]
find_stats(datalist)

######### TESTING PART 1: DISPLAY DATA ###################
'''
data1 = Data("254 Wellington", "P", "A", "E:/Work Study AIr Pollution Research/254 Wellington/254 wellington st n (outside) (43.254591 -79.863272) Primary Real Time 06_26_2019 10_10_2020.csv")
print(data1.Temperature)
temp=data1.find_mean("Temperature")
humidity=data1.find_mean("Humidity")
print(data1.channel)
print(temp)
print(humidity)

def print_stuff(temp, humidity):
    print(
        "Mean temp (F): {0} \n"
        "Mean humidity (%): {1} \n"
        "----------------------------------------------- \n".format(str(temp),str(humidity))
    )
print_stuff(temp,humidity)
'''
