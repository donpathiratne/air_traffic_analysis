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
            
        if i[-1][0:2]<'15':# check the value only below 15
            func5()

        if i[1][0:2]=='BA':# check only starting from 'BA' in flightNum
            func6()
        
        func7() # call the func7()
        func8() # call the func8()
        func9() # call the func9()
        func10() # call the func11()
        
        # create empty variables for counting destinations 
        count_lhr= count_mad= count_cdg= count_ist= count_ams= count_lis= count_fra= count_fco= count_muc= count_bcn= 0  
        destination_dict={} # empty dict
        for x in range(len(destination_list)):# get the length of destination_list and run a loop
            if destination_list[x] == 'LHR':                    # check list's data equal to LHR
                count_lhr += 1                                  # if equal, counting number of lhr
                destination_dict[airport_code['LHR']]=count_lhr # input the total count to lhr key in destination_dict

            elif destination_list[x] == 'MAD':                  # check list's data equal to MAD
                count_mad += 1                                  # if equal, counting number of MAD
                destination_dict[airport_code['MAD']]=count_mad # input the total count to MAD key in destination_dict

            elif destination_list[x] == 'CDG':                  # check list's data equal to CDG
                count_cdg += 1                                  # if equal, counting number of CDG
                destination_dict[airport_code['CDG']]=count_cdg # input the total count to CDG key in destination_dict

            elif destination_list[x] == 'IST':                  # check list's data equal to IST
                count_ist += 1                                  # if equal, counting number of IST
                destination_dict[airport_code['IST']]=count_ist # input the total count to IST key in destination_dict

            elif destination_list[x] == 'AMS':                  # check list's data equal to AMS
                count_ams += 1                                  # if equal, counting number of AMS
                destination_dict[airport_code['AMS']]=count_ams # input the total count to AMS key in destination_dict

            elif destination_list[x] == 'LIS':                  # check list's data equal to LIS
                count_lis += 1                                  # if equal, counting number of LIS
                destination_dict[airport_code['LIS']]=count_lis # input the total count to LIS key in destination_dict

            elif destination_list[x] == 'FRA':                  # check list's data equal to FRA
                count_fra += 1                                  # if equal, counting number of FRA
                destination_dict[airport_code['FRA']]=count_fra # input the total count to FRA key in destination_dict

            elif destination_list[x] == 'FCO':                  # check list's data equal to FCO
                count_fco += 1                                  # if equal, counting number of FCO
                destination_dict[airport_code['FCO']]=count_fco # input the total count to FCO key in destination_dict

            elif destination_list[x] == 'MUC':                  # check list's data equal to MUC
                count_muc += 1                                  # if equal, counting number of MUC
                destination_dict[airport_code['MUC']]=count_muc # input the total count to MUC key in destination_dict

            elif destination_list[x] == 'BCN':                  # check list's data equal to BCN
                count_bcn += 1                                  # if equal, counting number of BCN
                destination_dict[airport_code['BCN']]=count_bcn # input the total count to BCN key in destination_dict
            else:
                print('something went wrong') # unless it will print this msg
                
        least_destination_list=[] # empty list
        least_common_value= min(destination_dict.values()) # get minimum value in destination_dict values
        for y in destination_dict: # run a loop by using destination_dict
            if destination_dict[y]== least_common_value: # check least_common_value equals to destination_dict value
                least_destination_list.append(y) # append least_common_value to least_destination_list
        return least_destination_list # to get result after


    least_destination_list = main2() # call main2() function and assign value to least_destination_list

    print(f'The total number of flights from this airport was {count_list}')
    print(f'The total number of flights departing Terminal Two was {total_terminal_2}')
    print(f'The total number of departures on flights under 600 miles was {destination_miles}')
    print(f'There were {air_france} Air France flights from this airport')
    print(f'There were {temperature_below_15} flights departing in temperatures below 15 degrees')
    print(f'There was an average of {round(avg_per_hour,2)} British Airways flights per hour from this airport')
    print(f'British Airways planes made up {round(percentage_british_airway,2)}% of all departures')
    print(f'{percentage_delay_air_france}% of Air France departures were delayed')
    print(f'There were {len(count_rain)} hours in which rain fell')
    print(f'The least common destinations are {least_destination_list}')

    # Task C
    def main3():    
        with open("result.txt", "a") as f:      # create a result.txt file and append above outputs without overwritting
            f.write(('****************************************************************************\n'))
            f.write((f' File {selected_data_file} selected - Planes departing {airport_code[city_code]} {year}\n'))
            f.write(('****************************************************************************\n'))

            f.write(f'The total number of flights from this airport was {count_list}\n')
            f.write(f'The total number of flights departing Terminal Two was {total_terminal_2}\n')
            f.write(f'The total number of departures on flights under 600 miles was {destination_miles}\n')
            f.write(f'There were {air_france} Air France flights from this airport\n')
            f.write(f'There were {temperature_below_15} flights departing in temperatures below 15 degrees\n')
            f.write(f'There was an average of {round(avg_per_hour,2)} British Airways flights per hour from this airport\n')
            f.write(f'British Airways planes made up {round(percentage_british_airway,2)}% of all departures\n')
            f.write(f'{percentage_delay_air_france}% of Air France departures were delayed\n')
            f.write(f'There were {count_rain} hours in which rain fell\n')
            f.write(f'The least common destinations are {least_destination_list}\n')
            f.close()

        with open("result.txt", "r") as f:  # read the result.txt file
            f.read()
            f.close()

    main3()

    # Task D
    def main4():
        two_airline_code = input("Enter a two-character Airline code to plot a histogram: ").upper() # get two letter airline code and convert them uppercase
        while True:
            if two_airline_code not in air_line: # check two airline code that not available in air_line dict
                print('Unavailable Airline code please try again.')
                two_airline_code= input("Enter the two-character Airline code to plot a histogram: ").upper() # get two airline code again and convert it into upper
                continue
            else:
                break
        return two_airline_code # to get two airline code value after

    two_airline_code = main4()  # call main4() function and return two airline code value and assign it to two airine code

def main5():
        # create empty variables from count_00 to count_11
        count_00= count_01= count_02= count_03= count_04= count_05= count_06= count_07= count_08= count_09= count_10= count_11 = 0
        for y in data_list: # data_list assign to y line by line
            if two_airline_code == y[1][0:2]: # check two airline code equals to index[1][0:2] in data list   
                if y[2][0:2] == '00':
                    count_00 += 1       # if it equals to 00, count it
                elif y[2][0:2]== '01':
                    count_01 += 1       # if both equal to 01, count it
                elif y[2][0:2] == '02':
                    count_02 += 1       # if both equal to 02, count it
                elif y[2][0:2] == '03':
                    count_03 += 1       # if both equal to 03, count it
                elif y[2][0:2] == '04':
                    count_04 += 1       # if both equal to 04, count it
                elif y[2][0:2] == '05':
                    count_05 += 1       # if both equal to 05, count it
                elif y[2][0:2] == '06':
                    count_06 += 1       # if both equal to 06, count it
                elif y[2][0:2] == '07':
                    count_07 += 1       # if both equal to 07, count it
                elif y[2][0:2] == '08':
                    count_08 += 1       # if both equal to 08, count it
                elif y[2][0:2] == '09':
                    count_09 += 1       # if both equal to 09, count it
                elif y[2][0:2] == '10':
                    count_10 += 1       # if both equal to 10, count it
                elif y[2][0:2] == '11':
                    count_11 += 1       # if both equal to 11, count it
                else:
                    pass                # unless ignore it

        # create a departure_count_list and assign above count values to it
        departure_count_list =[count_00, count_01, count_02, count_03, count_04, count_05, count_06, count_07, count_08, count_09, count_10, count_11]
        return departure_count_list

    departure_count_list = main5()  # call the main5() function and get departure_count_list value and assign it 

    hours = ['00','01','02','03','04','05','06','07','08','09','10','11']   # create a hours list

