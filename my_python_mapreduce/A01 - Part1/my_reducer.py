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

#---------------------------------------
#  FUNCTION get_key_value
#---------------------------------------
def get_key_value(line):
    # 1. We create the output variable
    res = ()

    # 2. We remove the end of line char
    line = line.replace('\n', '')

    # 3. We get the key and value
    words = line.split('\t')
    station = words[0]
    value = words[1]

    # 4. We process the value
    value = value.rstrip(')')
    value = value.strip('(')
    num_ran_outs = int(value)

    # 4. We assign res
    res = (station, num_ran_outs)

    # 5. We return res
    return res

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    # 1. I create a dictionary with all the different stations in the file
    current_station = ""
    current_amount = 0

    # 2. I create a dictionary where I will add the stations ordered from the one with highest run outs to the lowest
    my_dict = {}

    # 3. I traverse the file content, to populate the data
    for line in my_input_stream:
        # 3.1. I get the info from the line
        stations = get_key_value(line)

        station = stations[0]
        num_ran_outs = int(stations[1])

        # 3.2. If current station == station then we update the number of run outs
        if station == current_station:
            current_amount = current_amount + num_ran_outs
        # 3.3. If the station is a new one
        else:
            if current_station != "":
                my_dict[current_station] = current_amount

            # 3.3.2. I reset the current station to be the new one
            current_station = station
            current_amount = num_ran_outs

    # 4. I add the last station data to the dictionary
    if current_station != "":
        my_dict[current_station] = current_amount

    # 5. I reverse the dictionary by the value
    my_sorted_dict = sorted(my_dict, key=my_dict.get, reverse=True)

    # 6. I write the result into the file
    for r in my_sorted_dict:
        station = r
        amount = my_dict[r]
        my_str = station + "\t(" + str(amount) + ")\n"
        my_output_stream.write(my_str)


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
    my_reducer(my_input_stream, my_output_stream, my_reducer_input_parameters)

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
    input_file_example = "../../my_result/A01 - Part1/my_sort_results.txt"
    output_file_example = "../my_result/A01 - Part1/my_reducer_results.txt"

    # 3. my_reducer.py input parameters
    # We list the parameters here

    # We create a list with them all
    my_reducer_input_parameters = []

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
           )
