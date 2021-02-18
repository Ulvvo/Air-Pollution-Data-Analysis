# Air-Pollution-Data-Analysis
Statistical analysis on the primary data collected by PurpleAir Monitors in Hamilton, Ontario during my Work Study term as an Undergraduate Research Assistant in the Department of Geography, Geomatics and Environment at the University of Toronto, under Professor Matthew Adams. The data analysis consists of finding descriptive statistics on the PM2.5 concentrations and finding the correlation between the sensors A and B for each monitor, to assess its reliability. Additionally, there is some bivariate analysis on the effect of environmental parameters like temperature and humidity on the PM2.5 concentration.

# Base code
Classes_functions.py contains all the base code for all the files: converts CSV files into Data objects for each monitor according to its measured parameters

# Descriptive statistics
dataanalysis.py contains functions and instructions to calculate basic descriptive statistics for each monitor: mean & standard deviation.
trial_functions.py contains functions to calculate several descriptive statistics.
Summary of Statistics.xlsx contains the mean and standard deviation of PM2.5 concentrations for all the monitors

# Correlation coefficient for each sensor
correlation.py contains all the functions and instructions to find a weekly pearson correlation coefficient for the PM2.5 concentrations for each sensor.
Correlationfinal.xlsx is an Excel sheet containing all the coefficient data for the monitors.
Correlationformatted.docx contains the formatted coefficients (word table format).

# Bivariate data
bivariate.py contains matplotlib code used to plot the relationships between temperature, humidity and PM2.5 concentrations. Humidity.png and Temperature.png are the figures plotted from the code.



