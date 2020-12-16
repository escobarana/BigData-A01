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

import sys
import codecs
from datetime import datetime, time as datetime_time, timedelta


# ---------------------------------------
#  FUNCTION get_key_value
# ---------------------------------------
def get_key_value(line):
    # 1. We create the output variable
    res = ()

    # 2. We remove the end of line char
    line = line.replace('\n', '')

    # 3. We get the key and value
    words = line.split('\t')
    day = words[0]
    hour = words[1]

    # 4. We process the value
    hour = hour.rstrip(')')
    hour = hour.strip('(')

    # 4. We assign res
    res = (day, hour)

    # 5. We return res
    return res


# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    # 1. I create necessary variables
    # 1.1 Number of total runouts in a row
    runouts = 0
    # 1.2 The actual time, when the run out started
    actual_time = ""
    # 1.3 Store data from the previous iteration to compare
    previous_time = ""
    previous_date = ""
    # 1.4 Add results to a list
    my_list = []
    # 1.5 Input parameter that contains the time difference in minutes between times in the csv's
    minutesdiff = int(my_reducer_input_parameters[0])

    # 2. I iterate through each line of the input file
    for line in my_input_stream:
        # 2.1. I get the info from the line
        data = get_key_value(line)
        current_date = data[0]
        current_time = data[1]

        # 2.2 First line
        if previous_date == "":
            previous_date = str(current_date)
            actual_time = str(current_time)  # set the actual time to be printed later
            previous_time = str(current_time)
            runouts = runouts + 1
        # 2.3 Remaining lines
        else:
            # 2.3.1 Same date -> continue
            if str(previous_date) == str(current_date):
                # 2.3.1.1 Five minutes difference between times -> sum 1 to runouts and update time
                if fivemindifference(current_time, previous_time, minutesdiff):
                    runouts = runouts + 1
                    previous_time = current_time
                # 2.3.1.2 Not 5 minutes difference between times -> update data and add previous data to a list
                else:
                    msg = str(previous_date) + "\t(" + str(actual_time) + ", " + str(runouts) + ")"
                    my_list.append(msg)
                    previous_date = str(current_date)
                    actual_time = str(current_time)  # set the actual time to be printed later
                    previous_time = str(current_time)
                    runouts = 1  # Count this iteration
            # 2.3.2 Different date -> Update data and add previous data to a list
            else:
                msg = str(previous_date) + "\t(" + str(actual_time) + ", " + str(runouts) + ")"
                my_list.append(msg)
                previous_date = str(current_date)
                actual_time = str(current_time)  # set the actual time to be printed later
                previous_time = str(current_time)
                runouts = 1  # Count this iteration

    # 3. I print the very last date
    if (current_date != ""):
        msg = str(previous_date) + "\t(" + str(actual_time) + ", " + str(runouts) + ")"
        my_list.append(msg)

    # 4. Iterate through the list and write the data to the output file
    for each in my_list:
        my_output_stream.write(each + "\n")


# ------------------------------------------
# FUNCTION fivemindifference
# ------------------------------------------
def fivemindifference(current_time, previous_time, minutesdiff):
    # 1. Define output variable
    res = False

    # 2. Split the previous time by hour min seg in order to sum the 5 minutes
    paramsP = previous_time.split(":")

    # 3. Sum 5 minutes to previous time
    tdelta = timedelta(hours=int(paramsP[0]), minutes=int(paramsP[1]), seconds=int(paramsP[2])) + timedelta(
        minutes=int(minutesdiff))

    # 4. Convert the result to datetime
    t = datetime.strptime(str(tdelta), "%H:%M:%S")

    # 5. Remove the "date" added by default when converting
    result = str(t).split(" ")
    time = result[1]

    # 6. Compare times -> previous_time + 5min = current_time
    if str(time) == str(current_time):
        res = True

    return res


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
            ):
    # 1. We select the input and output streams based on our working mode
    my_input_stream = None
    my_output_stream = None

    # 1.1: Local Mode --> We use the debug files
    if (local_False_Cloudera_True == False):
        my_input_stream = codecs.open(input_file_example, "r", encoding='utf-8')
        my_output_stream = codecs.open(output_file_example, "w", encoding='utf-8')

    # 1.2: Cloudera --> We use the stdin and stdout streams
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # 2. We trigger my_reducer
    my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters)


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Local Mode or Cloudera
    local_False_Cloudera_True = False

    # 2. Debug Names
    input_file_example = "../../my_result/A01 - Part3/2. my_sort_simulation/sort_1.txt"
    output_file_example = "../my_result/A01 - Part3/3. my_reduce_simulation/reduce_sort_1.txt"

    # 3. my_reducer.py input parameters
    # We list the parameters here
    measurement_time = 5

    # We create a list with them all
    my_reducer_input_parameters = [measurement_time]

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
            )
