from Code.classes_functions import Data
from _datetime import datetime, timedelta, date
import scipy
from scipy import stats

'''Functions'''
def convert_datetime(Data):
    '''
    Takes in a Data object and changes all the contents of its 'created_at' attribute from string objects to
    datetime objects.
    :param Data: Data object
    :return: a numpy array with datetime dates to represent created_at times

    Eg. Input: dataA = Data("Barrie","P","A", "{path of csv file containing data}")
    Command: list = convert_datetime(dataA)
    Output:
    [datetime.date(2019, 4, 6), datetime.date(2019, 4, 6), datetime.date(2019, 4, 6),...,datetime.date(2020, 10, 13),
    datetime.date(2020, 10, 13), datetime.date(2020, 10, 13), datetime.date(2020, 10, 13)]

    '''
    #access numpy array which contains all the created_at times as strings
    array = Data.created_at
    #create an empty list for the datetime objects
    list = []
    #use a 'for' loop to convert each string object in the array to a datetime object and append it to the list
    for i in array:
        i_datetime = datetime.strptime(i,'%Y-%m-%d %H:%M:%S %Z')
        list.append(i_datetime.date())
    return list

def find_closest(mylist,ending_date):
    ''' Takes in a list of datetime objects and an ending date for a specified week, and returns the closest date
    to the ending date within the list (that is greater than the ending_date). To be used when the ending_date is NOT
    in the list of dates when readings were taken/

    mylist: list of datetime objects when the readings were taken
    ending_date: the ending date of the given week

    Eg.
    Inputs:
    mylist = [datetime.date(2020, 10, 11), datetime.date(2020, 10, 13), datetime.date(2020, 10, 20)]
    ending_date1 = datetime.date(2020,10,14)
    ending_date2 = datetime.date(2020,10,10)
    ending_date3 = datetime.date(2020,10,12)

    Outputs:
    find_closest(mylist, ending_date1) = datetime.date(2020,10,20)
    find_closest(mylist, ending_date2) = datetime.date(2020,10,11)
    find_closest(mylist, ending_date3) = datetime.date(2020,10,13)
    '''
    # if the ending date is not in the list, we need to find the nearest one in the following week
    # a is the index of the date closest to the missing one
    a = min(range(len(mylist)), key=lambda i: abs(mylist[i] - ending_date))
    # b is the value of the nearest date to the missing one
    b = mylist[a]
    #check if the closest one (b) is greater than or less than the ending date
    if b<ending_date:
        # only keep the dates greater than the closest date
        new_list = [i for i in mylist if i>b]
        closest_date = new_list[0]
    elif b>ending_date:
        closest_date = b
    return closest_date

def week_indicesA(Data,start_date,end_date):
    '''
    Takes in a Data object FOR DATA CHANNEL A, its start date and end-date for observations
    Returns a list object with indices of dates representing each new week of readings:
    [start_date index=0, date2 index, date3 index ..., end_date index]

    Eg.
    Inputs:
    dataA = Data("Barrie","P","A", "{path of csv file containing data}")
    start_date = dataA.created_at[0] #first date of recording
    end_date = dataA.created_at[-1] #last date of recording

    Output:
    week_indicesA(dataA, start_date, end_date)
    ==>
    [0, 6747, 14280, 21838, 29390, 36947, 44499, 52035, 59456, 64495, 69526, 74566, 79604, 84642, 89681, 94721,
    99543, 104582, 109619, 114651, 119687, 124726, 129765, 134798, 139830, 144866, 149902, 154931, 159968, 165007,
    170047, 175070, 180110, 185148, 190093, 195131, 200170, 205210, 210250, 215242, 220282, 225322, 230362, 235200,
    240240, 245152, 250118, 255158, 260196, 265236, 270273, 275233, 280269, 285309, 290347, 295386, 300423, 305463,
    310487, 315525, 320551, 325589, 330629, 335663, 340702, 345724, 350739, 355734, 360771, 365808, 370825, 375864,
    380900, 385940, 390955, 395995, 401033, 406073, 411112, 416143]

    **Shows all the indices (i.e. rows of the data) where new week readings were taken
    '''
    #convert start date to datetime object
    start = datetime.strptime(start_date, '%Y-%m-%d')
    #convert end date to datetime object
    end = datetime.strptime(end_date, '%Y-%m-%d')
    # create dates array for created_at
    created_at_dates = convert_datetime(Data)
    #set current_date to start
    current_date = start.date()
    indices = [0]
    #ensure the current date is more than a week away from the end date
    while current_date <= (end.date()-timedelta(days=7)):
        #the week end is 7 days from the current date//start of new week
        ending_date = current_date + timedelta(days=7)
        #add the ending_index if the ending date is in created_at_dates
        if ending_date in created_at_dates:
            ending_index = created_at_dates.index(ending_date)
            current_date += timedelta(days=7)
        else:
            closest_date = find_closest(created_at_dates,ending_date)
            ending_index = created_at_dates.index(closest_date)
            current_date = closest_date
        indices.append(ending_index)
    return indices

def find_dates(wi_list,created_at_dates):
    '''
    Takes in a list of starting week indices of a Data object (as found from week_indicesA) and a list of all
    datetime objects corresponding to when readings were taken (as found from convert_datetime) and finds all the
    datetime objects corresponding to the week indices.

    Eg. Inputs:
    dataA = Data("Barrie","P","A", "{path of csv file containing data}")
    wi_list = week_indicesA(dataA)
    created_at_dates = convert_datetime(dataA)

    Output:

    find_dates(wi_list, created_at_dates)
    ==>
    #Returns a list of all the starting dates of each new week for readings. Sometimes the elapsed interval between
    dates are more than 7 days when monitors stop working but that is accounted for later.

    [datetime.date(2019, 4, 6), datetime.date(2019, 4, 13), datetime.date(2019, 4, 20), datetime.date(2019, 4, 27),
    datetime.date(2019, 5, 4), datetime.date(2019, 5, 11), datetime.date(2019, 5, 18), datetime.date(2019, 5, 25),
    datetime.date(2019, 6, 1), datetime.date(2019, 6, 8), datetime.date(2019, 6, 15), datetime.date(2019, 6, 22), ...,
    ..., datetime.date(2020, 9, 12), datetime.date(2020, 9, 19), datetime.date(2020, 9, 26), datetime.date(2020, 10, 3),
    datetime.date(2020, 10, 10)]

    '''
    dateslist = []
    for i in wi_list:
        dateslist.append(created_at_dates[i])
    return dateslist

def weekindicesB(dateslist_A, dataB):
    '''
    Takes in the starting date for new weeks for Data A object (as found in find_dates) and finds the indices
    for the matching dates in Data B object's created_at_dates list.

    :dateslist_A = find_dates(week_indicesA(dataA), convert_datetime(dataA))
    :dataB = Data(name of monitor, "P", "B", "{path of csv file}")

    If the date in A is not in B, the closest one within the week is found. If that is not found either, that week
    is discarded.
    Eg.
    Inputs:
    dataA = Data("Barrie","P","A", "{path of csv file containing data}")
    dl_A = find_dates(week_indicesA(dataA), convert_datetime(dataA))
    dataB = Data("Barrie","P","B", "{path of csv file containing data}")

    Output: week_indicesB(dl_A,dataB)
    ==>
    [0, 6746, 14277, 21834, 29386, 36942, 44488, 52020, 59440, 64479, 69510, 74550, 79589, 84628, 89667, 94707, 99528,
    104568, 109606, 114637, 119671, 124710, 129749, 134782, 139815, 144850, 149887, 154921, 159960, 164999, 170039,
     175062, 180102, 185142, 190086, 195124, 200160, 205200, 210240, 215232, 220272, 225311, 230351, 235190, 240230,
     245142, 250109, 255147, 260185, 265225, 270264, 275226, 280264, 285304, 290342, 295381, 300418, 305458, 310484,
      315523, 320550, 325588, 330628, 335665, 340705, 345727, 350747, 355744, 360782, 365818, 370837, 375877, 380912,
      385952, 390963, 396003, 401042, 406082, 411121, 416153]
    '''
    #convert Data B's created_at dates into datetime
    all_B = convert_datetime(dataB)
    #create an empty list for the A & B matching week beginning indices
    week_i = []
    for date in dateslist_A:
        #if the date in A's list is within B, add that date's corresponding B index into the week_i
        if date in all_B:
            week_i.append(all_B.index(date))
        #if the date in A's list not within B, the nearest one is found (that falls within a week of B) and is added to
        # week_i
        elif date not in all_B:
            cd = find_closest(all_B,date)
            if cd in range(date,date+timedelta(days=7)):
                week_i.append(all_B.index(cd))
    return week_i

def get_coeffs(dataA,dataB,startdate,enddate):
    '''
        Takes in two data objects and a start + end date for the observations -->
        outputs a dictionary with the week starting date as the key and the pearson coefficient as the value.

        Eg.
        Inputs:
        dataA = Data("Barrie","P","A", "{path of csv file containing data}")
        dataB = Data("Barrie","P","B", "{path of csv file containing data}")
        startdate = "2019-04-06" #using dataA.created_at[0]
        enddate = "2020-10-13" #using dataA.created_at[-1]
        #assume both A and B have the same starting and ending dates

        Output: get_coeffs(dataA,dataB,startdate,enddate)
        ==>
        {datetime.date(2019, 4, 6): 0.9696053398648334, datetime.date(2019, 4, 13): 0.990359669315833,
        datetime.date(2019, 4, 20): 0.9957281611717465, datetime.date(2019, 4, 27): 0.9939060232124205,
        datetime.date(2019, 5, 4): 0.9947088358826991, datetime.date(2019, 5, 11): 0.9788581861132205, .......
        .....,datetime.date(2020, 9, 19): 0.9977246627052291, datetime.date(2020, 9, 26): 0.9976778602210914,
        datetime.date(2020, 10, 3): 0.9893101896504817}

    '''
    # access PM 2.5 numpy arrays
    dataA_conc = dataA.PM25_ATM
    dataB_conc = dataB.PM25_ATM

    wi_A = week_indicesA(dataA,startdate,enddate)
    dateslistA = find_dates(wi_A,convert_datetime(dataA))
    wi_B = weekindicesB(dateslistA,dataB)
    dict = {}

    i = 0
    while i < len(wi_A)-1:
        arr1_all = dataA_conc[wi_A[i]:wi_A[i+1]]
        arr2_all = dataB_conc[wi_B[i]:wi_B[i+1]]
        if len(arr1_all)<len(arr2_all):
            arr2 = arr2_all[0:len(arr1_all)]
            arr1 = arr1_all
        else:
            arr1 = arr1_all[0:len(arr2_all)]
            arr2 = arr2_all
        pearsoncoeff = scipy.stats.pearsonr(arr1, arr2)[0]
        dict[dateslistA[i]]= pearsoncoeff
        i+=1
    return dict

def discontinued_weeks(dateslist):
    '''Finds all the weeks that are not continuous - aka have time gaps greater than 7 days between dates

    :dateslist = list of dates where the coefficients are taken

    Eg.
    Inputs:
    dataA = Data("Barrie","P","A", "{path of csv file containing data}")
    dataB = Data("Barrie","P","B", "{path of csv file containing data}")
    startdate = "2019-04-06" #using dataA.created_at[0]
    enddate = "2020-10-13" #using dataA.created_at[-1]
    coeffs = get_coeffs(dataA,dataB,startdate,enddate)
    dateslist = coeffs.keys() #take all the dates corresponding to when the coefficients are taken

    Output: discontinued_weeks(dateslist)
    ==> [] #aka there are no discontinued weeks in Barrie's recordings

    Eg. 2
    Inputs:
    dataA = Data("Grant Avenue and Stinson Street","P","A", "{path of csv file containing data}")
    dataB = Data("Grant Avenue and Stinson Street","P","B", "{path of csv file containing data}")
    startdate = "2019-05-27"#using dataA.created_at[0]
    enddate = "2020-01-06"  #using dataA.created_at[-1]
    coeffs = get_coeffs(dataA,dataB,startdate,enddate)
    dateslist = coeffs.keys() #take all the dates corresponding to when the coefficients are taken

    Output: discontinued_weeks(dateslist)
    ==>
    [datetime.date(2019, 8, 15), datetime.date(2019, 9, 15), datetime.date(2019, 9, 25), datetime.date(2019, 11, 8),
    datetime.date(2019, 11, 28), datetime.date(2019, 12, 20)]

    ^^ means that these dates are the new starting dates after a break longer than 7 days (1 week)
    '''
    i = 0
    weeks = []
    while i < len(dateslist)-2:
        if dateslist[i+1]==dateslist[i]+timedelta(days=7):
            i+=1
        elif dateslist[i+1]>dateslist[i]+timedelta(days=7):
            weeks.append(dateslist[i+1])
            i+=1
    return weeks



'''Testing Zone'''
'''Barrie'''
# data1 = Data("Barrie St. Dundas", "P", "A", "{path to CSV}")
# data2 = Data("Barrie St. Dundas", "P", "B", "{path to CSV}")
# c = get_coeffs(data1,data2,"2019-04-06","2020-10-13")
# discont = discontinued_weeks(list(c.keys()))

a = "Correlation: \n"
b = "\n Discontinued weeks: \n"
b2 = "\n All dates: \n"

#print(a,c.values(), b, discont, b2, c.keys())
