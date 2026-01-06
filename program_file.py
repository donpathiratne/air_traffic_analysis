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
