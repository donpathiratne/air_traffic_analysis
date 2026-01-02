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
