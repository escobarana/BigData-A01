#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import os
import codecs


# ------------------------------------------
#
# HIGHER ORDER FUNCTIONS
#
# ------------------------------------------

# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(funct, my_list):
    # 1. We create the output variable
    res = []

    # 2. We populate the list with the higher application
    for item in my_list:
        sol = funct(item)
        res.append(sol)

    # 3. We return res
    return res


# ------------------------------------------
# FUNCTION my_filter
# ------------------------------------------
def my_filter(funct, my_list):
    # 1. We create the output variable
    res = []

    # 2. We populate the list with the higher application
    for item in my_list:
        # 2.1. If an item satisfies the function, then it passes the filter
        if funct(item) == True:
            res.append(item)

    # 3. We return res
    return res


# ------------------------------------------
# FUNCTION my_fold
# ------------------------------------------
def my_fold(funct, accum, my_list):
    # 1. We create the output variable
    res = accum

    # 2. We populate the list with the higher application
    for item in my_list:
        res = res + funct(accum, item)

    # 3. We return res
    return res


# ------------------------------------------
#
# LINE PROCESSING
#
# ------------------------------------------

# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    # 1. We create the output variable
    res = ()

    # 2. We remove the end of line character
    line = line.replace("\n", "")

    # 3. We split the line by tabulator characters
    params = line.split(";")

    # 4. We assign res
    if (len(params) == 7):
        res = (int(params[0]), params[1], float(params[2]), float(params[3]), params[4], int(params[5]), int(params[6]))

    # 5. We return res
    return res


# ------------------------------------------
#
# TO DO
#
# ------------------------------------------

# ------------------------------------------
# FUNCTION nameAndBikes
# ------------------------------------------
def nameAndBikes(item):
    # 1. Create the result variable
    res = []

    # 2. I define a list of item
    mylist = list(item)

    # 3. I assign the variables
    name = mylist[1]
    bikes = mylist[5]

    # 4. I append them to the output variable
    res.append(name)
    res.append(bikes)

    # 5. Return the result in a tuple
    return tuple(res)


# ------------------------------------------
# FUNCTION nameAndBikesRunOut
# ------------------------------------------
def nameAndBikesRunOut(item):
    # 1. Create the output variable
    res = False

    # 2. I define a list of item
    mylist = list(item)

    # 3. Check if the runouts are 0
    if mylist[1] == 0:
        res = True

    # 4. Return the output
    return res


# ------------------------------------------
# FUNCTION desiredStations
# ------------------------------------------
def desiredStations(item, station_names):
    # 1. Create the result variable
    res = False

    # 2. I define a list of item
    mylist = list(item)

    # 3. Iterate through the names of the stations
    for each in station_names:
        # 3.1 I compare the name of the item to the ones in the station names list
        if mylist[0] == each:
            res = True

    # 4. Return the result
    return res


# ------------------------------------------
# FUNCTION nameAndOnes
# ------------------------------------------
def nameAndOnes(item):
    # 1. Create the result variable
    res = []

    # 2. I define a list of item
    mylist = list(item)

    # 3. Define the variable
    names = mylist[0]

    # 4. Add to the result list the data
    res.append(names)
    res.append(1)

    # Return the result as a tuple
    return tuple(res)


# ------------------------------------------
# FUNCTION totalRunOut
# ------------------------------------------
def totalRunOut(accum, item):
    # 1. Create the result variable and assign it the value of the parameter accum
    res = accum

    # 2. I define a list of item
    mylist = list(item)

    # 3. Define the variable
    runouts = mylist[1]

    # 4. Add the runouts to the result variable
    res = res + runouts

    # 5. Return the result variable
    return res


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(my_list, station_names):
    # --------------- STEP 1 ------------------------#

    # 1. Apply the Higher-Order function my_map provided above,
    #    so as to apply "process_line" to all functions

    my_list = my_map(lambda x: process_line(x), my_list)  # -> Replace None with a call to my_map

    print("\n\n\n\n\n------ STEP 1 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 2 ------------------------#

    # 2. Apply the Higher-Order function my_map again,
    #    now to restrict the tuple previously computed to just the name of the station and the amount of bikes available
    my_list = my_map(lambda item: nameAndBikes(item), my_list)  # -> Replace None with a call to my_map

    print("\n\n\n\n\n------ STEP 2 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 3 ------------------------#

    # 3. Apply the Higher-Order function my_filter provided above,
    #    now to restrict only the entries which are ran out of bikes

    my_list = my_filter(lambda x: nameAndBikesRunOut(x), my_list)  # -> Replace None with a call to my_filter

    print("\n\n\n\n\n------ STEP 3 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 4 ------------------------#

    # 4. Apply the Higher-Order function my_filter again,
    #    now to restrict the entries to the ones of the desired stations

    my_list = my_filter(lambda x: desiredStations(x, station_names), my_list)  # -> Replace None with a call to my_filter

    print("\n\n\n\n\n------ STEP 4 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 5 ------------------------#

    # 5. Apply the the Higher-Order function my_map again,
    #    now to make each entry to be (Station_name, 1)

    my_list = my_map(lambda x: nameAndOnes(x), my_list)  # -> Replace None with a call to my_map

    print("\n\n\n\n\n------ STEP 5 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 6 ------------------------#

    # 6. Apply the the Higher-Order function my_fold provided above,
    #    so as to compute the total amount of ran outs

    res = my_fold(lambda x, i: totalRunOut(x, i), 0, my_list)  # -> Replace None with a call to my_fold

    print("\n\n\n\n\n------ STEP 6 ------\n")
    print(res)


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Local or HDFS folders
    input_file_name = "../../my_dataset/bikeMon_20170317.csv"
    output_file_name = "../../my_result/A01 - Part4/result.txt"

    # 2. List of stations we are interested into
    station_names = ["Fitzgerald's Park", "South Main St.", "Lapp's Quay"]

    # 3. We read-in the content from the input file

    # 3.1. We open the file for reading
    my_input_stream = codecs.open(input_file_name, "r", encoding='utf-8')

    # 3.2. We read-in its content
    file_content = []
    for line in my_input_stream:
        file_content.append(line)

    # 3.3. We close the file
    my_input_stream.close()

    # 4. We call to my_main
    my_main(file_content, station_names)
