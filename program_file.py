'''creating a airplane departures summeraization programe.'''
from graphics import *
import csv
import math

data_list = []   # data_list An empty list to load and hold data from csv file

def load_csv(CSV_chosen):
    """
    This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
    """
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)

selected_data_file="LHR2025.csv" #hard coded csv name to be replaced with your dynamically created filename
load_csv(selected_data_file)     #calls the function "load_csv" sending the variable 'selected_data_file" as a parameter

request = 'Y' # default value
while request== 'Y': # if equals, it will run
    data_list = []# clear data list
    # Task A
    airport_code={'LHR':'London Heathrow',
            'MAD':'Madrid Adolfo Suárez-Barajas',          # create a airport code dict
            'CDG':'Charles De Gaulle International',
            'IST':'Istanbul Airport International',
            'AMS':'Amsterdam Schiphol',
            'LIS':'Lisbon Portela',
            'FRA':'Frankfurt Main',
            'FCO':'Rome Fiumicino',
            'MUC':'Munich International',
            'BCN':'Barcelona International'}

    air_line= { 'BA':'British Airways',                     # create a air line code dict                
                'AF':'Air France',
                'AY':'Finnair' ,
                'KL':'KLM',
                'SK':'Scandinavian Airlines',
                'TP':'TAP Air Portugal', 
                'TK':'Turkish Airlines',
                'W6':'Wizz Air',
                'U2':'easyJet', 
                'FR':'Ryanair', 
                'A3':'Aegean Airlines', 
                'SN':'Brussels Airlines', 
                'EK':'Emirates', 
                'QR':'Qatar Airways', 
                'IB':'Iberia', 
                'LH':'Lufthansa'}

    def city_function():
        city_code=input('please enter a three-letter city code: ')   # get city code from user
        while True:
            if len(city_code)==3:               # check the length of city_code       
                city_code=city_code.upper()     # convert city code to uppercase
                if city_code in airport_code:   # check city code avaiable or not in airport code
                    break
                else:
                    city_code=input('Unavailable city code - please enter a valid city code: ')   # get city_code again because previous one not in airport code
                    continue
            else:
                city_code=input('Wrong code length – please enter a three-letter city code: ')    # get city_code again because previous one has wrong length
        return city_code    # to get city code value after


    def year_function():
        year=input('Please enter the year required in the format YYYY: ')   # get year from user
        while True:
            try:
                year=int(year)  # try to convert year string to integer 
                if year>=2000 and year<=2025:   # check year is from 2000 to 2025
                    break
                else:
                    year=input('Out of range - please enter a value from 2000 to 2025: ') # if year is out of range, get year again
                    continue
            except ValueError:  # unless convert it, it will give an error
                year=input('Wrong data type - please enter a four-digit year value: ')# get year again 
        return year

    def data_file_fuction():
        selected_data_file = city_code+ ''+ str(year)+ '.csv'    # assigning created csv file to selected_data_file
        try:
            load_csv(selected_data_file)
            print('****************************************************************************')
            print(f' File {selected_data_file} selected - Planes departing {airport_code[city_code]} {year}') # make the print statement
            print('****************************************************************************')
        except:
            print('File not Found.')
            exit()  #  exit the python program
        return selected_data_file



    city_code = city_function() # call the city_fuction and return city code value and assign to city_code
    year = year_function()          # call the year_function and return the year and assign to year
    selected_data_file = data_file_fuction()    # call data_file_function and return selected data file value and assign it

    # Task B 

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

    # create a Histogram
    def histogram():
        win = GraphWin('Hitogram', 900, 600) # create a graph window
        win.setCoords(0,0,900,600) # set the coordinate system of the window

        title_1 = Text(Point(450,580), f'Departures by hour for {air_line[two_airline_code]} from {airport_code[city_code]} {year}') # create a upper text part
        title_1.setStyle('bold') # bold the title1 text
        title_1.draw(win) # draw the text

        title_2 = Text(Point(30, 300), 'Hours\n\n00:00\nto\n12:00') # create a left side title
        title_2.draw(win) # draw the text

        
        vertical_line = Line(Point(90,30),Point(90,559)) # create a vertical line
        vertical_line.draw(win) # draw the vertical line

        y = 559 # starting left corner y point of rectangle 
        z = 536 # starting right corner y point of rectangle
        c = 0 # create a empty variable
        maximum = max(departure_count_list) # get maximum value
        if maximum<8: # check maximum less than 8
            pix= 90
        elif maximum<16:# check maximum less than 16
            pix= 65
        elif maximum <30:# check maximum less than 30
            pix= 30
        elif maximum >100:# check maximum greater than 100
            pix= 1

        for b in departure_count_list:
            rectangle_loop = Rectangle(Point(90,y),Point(90+b*pix,z)) # create rectangles 
            rectangle_loop.setFill('pink') # set them into pink color
            rectangle_loop.draw(win) # draw the rectangles

            point_start= rectangle_loop.getP1() # get left upper corner point each rectangle
            point_start.move(-15, -12.5) # change its position
            point_start_x = point_start.getX() # get its new x position
            point_start_y = point_start.getY() # get its new y position
            text_start = Text(Point(point_start_x, point_start_y), hours[c]) # set values in hours list in new position
            text_start.draw(win) # draw the texts

            point_final= rectangle_loop.getP2() # get right below corner point each rectangles
            point_final.move(10,12.5) # change its position
            point_final_x= point_final.getX() # get new x position
            point_final_y= point_final.getY() # get new y position
            text_final = Text(Point(point_final_x, point_final_y), b) # set values in departure_count_list in new position
            text_final.draw(win)

            y = y - 23*2 # create 23 pixcel width size rectangle and put 23 pixcel spaces between each rectangles
            z = z - 23*2 
            c += 1
        win.getMouse() # when click the mouse on graph window, it will closes
        win.close()

    histogram() # call the histogram function

    request = input('Do you want to select a new data file? Y/N:').upper() # get user input to run program again it convert upper

else:
    # Task E
    print('Thank you. End of Run.') # end the program
# End
