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

    def find_size(self, attribute):
        array=self.__getattribute__(attribute)
        size = len(array)
        return size
    def find_missing(self):
        missing = self.all_data.isnull().sum()
        print("Number of missing values in each column:")
        print(missing)

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

    def find_min(self,attribute):
        array = self.__getattribute__(attribute)
        min = np.amin(array)
        return min

    def find_max(self,attribute):
        array = self.__getattribute__(attribute)
        max = np.amax(array)
        return max

    def find_var(self,attribute):
        '''
       :param attribute: string name of the Data Object attribute
        :return: float
        Takes in an attribute as a string. Finds corresponding array as an attribute of the Data object
        Calculates the variance of all the elements inside it.
        '''
        array = self.__getattribute__(attribute)
        var = np.var(array)
        return var

