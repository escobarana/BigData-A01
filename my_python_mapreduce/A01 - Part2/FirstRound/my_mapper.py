#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Pythozoon interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys
import codecs


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
        res = tuple(params)

    # 5. We return res
    return res


# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(my_input_stream, my_output_stream, my_mapper_input_parameters):
    # Define variables
    # 1.2 I define the output variable
    res = 0
    # 1.2 I define the input parameter
    input_name = my_mapper_input_parameters[0]

    # 2. I iterate trough the input stream and process each line
    for line in my_input_stream:
        # 2.1 I process each lines in the csv
        stations = process_line(line)

        # 2.2 Define the variables for a better understanding
        name = stations[1]
        status = int(stations[0])
        bikes_available = int(stations[5])

        # 2.3 If the station is the one from the input parameters and also it satisfies the condition I add 1 to the
        # output variable
        if name == str(input_name) and status == 0 and bikes_available == 0:
            res = res + 1

    # 3. Write the output variable into the file
    msg = "total\t(" + str(res) + ")\n"
    my_output_stream.write(msg)


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(local_False_Cloudera_True,
            my_mapper_input_parameters,
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

    # 2. We trigger my_map
    my_map(my_input_stream, my_output_stream, my_mapper_input_parameters)


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
    input_file_example = "../../../my_dataset/bikeMon_20170204.csv"
    output_file_example = "../../../my_result/A01 - Part2/FirstRound/my_mapper_results.txt"

    # 3. my_mappper.py input parameters
    # We list the parameters here
    station_name = "Fitzgerald's Park"

    # We create a list with them all
    my_mapper_input_parameters = [station_name]

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_mapper_input_parameters,
            input_file_example,
            output_file_example
            )
