'''air traffic analising program'''

from graphics import *
import csv
import math

data_list = [] # data_list is an empty list to load and hold data from csv file

'''get data and append them to data_list'''
def load_csv(csv_chosen):
    with open(csv_chosen,'r') as file:
        csvreader= csv.reader(file)
        header= next(csvreader)
        for row in csvreader:
            data_list.append(row)

# create the air port code dictionary
airport_code= {'LHR': 'London Heathrow',
               'MAD': 'Madrid Adolfo Suarez-Barajas',
               'CDG': 'Charles De gaulle International',
               'IST': 'Istanbul Airport International',
               'AMS': 'Amsterdam Schiphol',
               'LIS': 'Lisbon portela',
               'FRA': 'Frankfurt main',
               'FCO': 'Rome Fiumicino',
               'MUC': 'Munich International',
               'BCN': 'Barcelona International'
               }

# create a air line code dict
air_line= {'BA': 'British Airways',
           'AF': 'Air france',
           'AY': 'Finnair',
           'KL': 'KLM',
           'SK': 'Scandinavian Airlines',
           'TP': 'TAP Air Portugal',
           'TK': 'Turkish Airlines',
           'W6': 'Wizz Air',
           'U2': 'easyJet',
           'FR': 'Ryanair',
           'A3': 'Aegean Airlines',
           'SN': 'Brussels Airlines',
           'EK': 'Emirates',
           'QR': 'Qutar Airways',
           'IB': 'Iberia',
           'LH': 'Lufthansa'}

'''get city code from user'''
def city_fuction():
    city_code= input('please enter a three-letter city code: ')
    while True:
        if len(city_code) == 3: # check that city code length is 3 
            city_code=city_code.upper()
            if city_code in airport_code: # check city code in airport code
                break
            else:
                city_code= input('Unavilable city code - please enter a three letter city code: ')
                continue
        else:
            city_code= input('wrong code length - please enter a three letter city code: ')
    return city_code

'''get year from user'''
def year_function():
    year= input('Please enter the year required in the format YYYY:')
    while True:
        try:
            year= int(year) # check is it correct data type
            if year<=2000 and year<=2025: # check the year within the range
                break
            else:
                year= input('Out of range - please enter a value from 2000 to 2025: ')
                continue
        except:
            year= input('Wrong data type - please enter a four digit year value: ') 
    return year

'''create selected data file and display the related file with year that has been chosen by user.'''
def data_file_function():
    selected_data_file= city_code+ ''+ str(year)+ '.csv'
    try:
        print('*'*50)
        print(f'{selected_data_file} selected - Planes departing {airport_code[city_code]}  {year}')
        print('*'*50)
    except:
        print('File not found.')
        exit()
    return selected_data_file

'''call all above functions and return their values'''
city_code= city_function()
year= year_function()
selected_data_file= data_file_function()

'''create variables'''
count_list= 0
total_terminal_2=  0
destination_miles= 0
air_france= 0
temperature_below_15= 0
british_airways= 0
avg_per_hour= 0
percentage_british_airway= 0
delay_air_france= 0
percentage_delay_air_france= 0
count_rain= []
destination_list= []

def main2():
    def func1():
        global count_list
        count_list=count_list+1 # counting total of data lists in selected data file  

    def func2():
        global total_terminal_2
        total_terminal_2=total_terminal_2 + 1 # counting number of flights departing from Terminal two
        
    def func3():
        global destination_miles       
        destination_miles=destination_miles + 1 # counting number of departuer flights under 600 miles

    def func4():
        global air_france
        air_france=air_france + 1 # counting Air France aircrafts
        return air_france # to get air_farance value later
        
    def func5():    
        global temperature_below_15   
        temperature_below_15=temperature_below_15 + 1   # counting number of flights departing in temperatures below 15 
    
    def func6():
        global british_airways, avg_per_hour       
        british_airways=british_airways + 1 # counting number of british airways 
        avg_per_hour=british_airways / 12 # the average number of British Airways departures per hour

    def func7():
        global percentage_british_airway
        percentage_british_airway= (british_airways / count_list) * 100 # counting the percentage of total departures that are British Airways aircraft
    
    def func8():
    global percentage_delay_air_france, delay_air_france
    try:
        if i[3]!=i[2] and i[1][0:2]=='AF': # check sheduled and actual departures are not same in air france
            delay_air_france=delay_air_france + 1 # count number of delay air france
        if air_france>0:
            percentage_delay_air_france=round((delay_air_france / air_france)* 100,2) # cannot divide by zero
        else:
            percentage_delay_air_france='0.0'
    except ZeroDivisionError:
        percentage_delay_air_france='0.0' # unless it will give an zerodivision error
    def func9():
        global count_rain
        if i[-1][-4:]=='rain': # only get rain includes
            if i[2][0:2] == '00': # check it equals to 00
                if '00' not in count_rain: # check 00 not in count_rain list
                    count_rain.append('00') # append to the list 
            elif i[2][0:2] == '01':# check it equals to 01
                if '01' not in count_rain:# check 01 not in count_rain list
                    count_rain.append('01')
            elif i[2][0:2] == '02':# check it equals to 02
                if '02' not in count_rain:# check 02 not in count_rain list
                    count_rain.append('02')
            elif i[2][0:2] == '03':# check it equals to 03
                if '03' not in count_rain:# check 03 not in count_rain list
                    count_rain.append('03')
            elif i[2][0:2] == '04':# check it equals to 04
                if '04' not in count_rain:# check 04 not in count_rain list
                    count_rain.append('04')
            elif i[2][0:2] == '05':# check it equals to 05
                if '05' not in count_rain:# check 05 not in count_rain list
                    count_rain.append('05')
            elif i[2][0:2] == '06':# check it equals to 06
                if '06' not in count_rain:# check 06 not in count_rain list
                    count_rain.append('06')
            if i[2][0:2] == '07':# check it equals to 07
                if '07' not in count_rain:# check 07 not in count_rain list
                    count_rain.append('07')
            if i[2][0:2] == '08':# check it equals to 08
                if '08' not in count_rain:# check 08 not in count_rain list
                    count_rain.append('08')
            if i[2][0:2] == '09':# check it equals to 09
                if '09' not in count_rain:# check 09 not in count_rain list
                    count_rain.append('09')
            if i[2][0:2] == '10':# check it equals to 10
                if '10' not in count_rain:# check 10 not in count_rain list
                    count_rain.append('10')
            if i[2][0:2] == '11':# check it equals to 11
                if '11' not in count_rain:# check 11 not in count_rain list
                    count_rain.append('11')
            else:
                pass # unless it will not count 
            
    def func10():
        destination_list.append(i[4])# append destination to the destination list

    for i in data_list:
        func1() # call the func1()
    
        if i[8]=='2': # check index 8 equals to '2'
            func2() # call the func2()
    
        if int(i[5])<600: # check distace mile is under 600
            func3() # call the func3()
    
        if i[1][0:2]=='AF': # check Air France air craft
            func4()# call the func4()

