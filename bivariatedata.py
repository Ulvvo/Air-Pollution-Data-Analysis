import matplotlib.pyplot as plt
from Code.classes_functions import Data
import numpy as np

plt.interactive(True)

data1 = Data("254 Wellington", "P", "A", "E:/Work Study AIr Pollution Research/254 Wellington/254 wellington st n (outside) (43.254591 -79.863272) Primary Real Time 06_26_2019 10_10_2020.csv")
x = data1.Humidity
y = data1.PM25_ATM
'''
plt.scatter(x,y)
plt.show(block=True)
'''
def scatter(Data0bject,x_var, y_var, x_label, y_label, graph_title):
    '''
    Takes in a Data object and strings describing the x and y parameters you want to plot against each other
    :param Data0bject: Data object (Data Frame)
    :param x_var: Name of independent parameter (String)
    :param y_var: Name of dependent parameter (string)
    :return: a scatter plot
    '''
    x = Data0bject.__getattribute__(x_var)
    y = Data0bject.__getattribute__(y_var)
    plt.scatter(x,y,s=None, c=None,marker='.')
    axes = plt.gca()
    #axes.set_xlim([xmin, xmax])
    axes.set_ylim([0, 80])

    (m,c) = np.polyfit(x,y,1)
    y2 = m*x+c
    plt.plot(x,y2,'r-',label="Line of best fit")
    plt.legend()
    '''Plot formatting'''
    plt.xlabel('{0}'.format(x_label))
    plt.ylabel('{0}'.format(y_label))
    plt.title("{0}".format(graph_title))

    plt.show(block=True)

scatter(data1,"Humidity","PM25_ATM","Relative Humidity (%)","Concentration of " + r'$PM_{2.5} $' + " " + r'$(\mu g /m^{3})$', "Effect of Humidity on "+ r'$PM_{2.5} $' + " Concentration")
scatter(data1,"Temperature","PM25_ATM","Temperature " + r"$^\circ F$","Concentration of " + r'$PM_{2.5} $' + " " + r'$(\mu g /m^{3})$', "Effect of Temperature on "+ r'$PM_{2.5} $' + " Concentration")

''' 
#####Test code###########
a=np.array([0,1,2,3,4])
b=2*a
plt.plot(a,b)
plt.title("Concentration of " + r'$PM_{2.5} $' + " " + r'$(\mu g /m^{3})$')
plt.show(block=True)
'''