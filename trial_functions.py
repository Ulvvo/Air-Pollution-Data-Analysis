import csv
import pandas as pd
import numpy as np

'''
Eventually, can clean up data and use OOP with Data as a Class
'''

#Parse csv file containing pollutant parameters data and convert it into a Pandas DataFrame
All_data = pd.read_csv("E:/Work Study AIr Pollution Research/254 Wellington/254 wellington st n (outside) (43.254591 -79.863272) Primary Real Time 06_26_2019 10_10_2020.csv")
print(All_data)

#Convert specific columns of the Pandas dataframe into an Numpy array
created_at = All_data["created_at"].to_numpy()
entry_id = All_data["entry_id"].to_numpy()
PM1_CF1 = All_data["PM1.0_CF1_ug/m3"].to_numpy(dtype=float)
PM25_CF1 = All_data["PM2.5_CF1_ug/m3"].to_numpy(dtype=float)
PM10_CF1 = All_data["PM10.0_CF1_ug/m3"].to_numpy(dtype=float)
PM25_ATM = All_data["PM2.5_ATM_ug/m3"].to_numpy(dtype=float)
RSSI_dbm = All_data["RSSI_dbm"].to_numpy(dtype=int)
Temperature = All_data["Temperature_F"].to_numpy(dtype=int)
Humidity = All_data["Humidity_%"].to_numpy(dtype=int)

def find_mean(array):
    '''(array) --> (float)
    Takes in a numpy array and calculates the mean of all the elements inside it'''
    mean = np.mean(array)
    return mean
def find_median(array):
    '''(array) --> (float)
    Takes in a numpy array and calculates the median from all the elements inside it'''
    median = np.median(array)
    return median
def find_sd(array):
    '''
    :param array: numpy array
    :return: float
    Takes in numpy array and calculates the standard deviation of all the elements inside it
    '''
    sd = np.std(array)
    return sd
def find_var(array):
    '''
    :param array: numpy array
    :return: float
    Takes in numpy array and calculates the variation of all the elements inside it
    '''
    var = np.var(array)
    return var
print(find_mean(PM1_CF1),find_median(PM1_CF1),find_sd(PM1_CF1),find_var(PM1_CF1))

