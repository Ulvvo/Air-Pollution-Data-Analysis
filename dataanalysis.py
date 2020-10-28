from classes_functions import Data, display_data, find_stats

### THIS IS THE FILE THAT CALCULATES STATISTICAL MEASURES (MEAN & STANDARD DEVIATION) OF DATA ###

'''
CREATE Data objects from the given information: Monitor name, Primary or Secondary data ("P" or "S"),
Channel A or B ("A" or "B"), and link to given CSV file.

eg. 254 Wellington Primary Monitor A Data
data = Data("254 Wellington", "P", "A", "E:/Work Study AIr Pollution Research/254 Wellington/254 wellington st n (outside) (43.254591 -79.863272) Primary Real Time 06_26_2019 10_10_2020.csv")
'''
### ADD THE MONITOR NAME AND LINKS BELOW: create as many as needed ###
data1 = Data("<insert monitor name>", "P", "A","<insert link to corresponding CSV file on your computer>")
data2 = Data ("<insert monitor name>", "S", "A","<insert link to corresponding CSV file on your computer>")
data3 = Data ("<insert monitor name>", "P", "B","<insert link to corresponding CSV file on your computer>")
data4 = Data ("<insert monitor name>", "S", "B","<insert link to corresponding CSV file on your computer>")
# ....(more data objects)...


### LIST OF ALL THE Data objects: add more as needed ###
Datalist = [data1,data2,data3,data4]

### CONDUCT STATISTICAL ANALYSIS ON THE LIST ###
'''Returns a display of the mean and standard deviations of all the relevant pollutant parameters'''
find_stats(Datalist)
