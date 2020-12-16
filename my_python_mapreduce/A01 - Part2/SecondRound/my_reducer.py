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
    time = words[0]
    value = words[1]

    # 4. We process the value
    value = value.rstrip(')')
    value = value.strip('(')
    num_ran_outs = int(value)

    # 4. We assign res
    res = (time, num_ran_outs)

    # 5. We return res
    return res

#---------------------------------------
#  FUNCTION print_key_value
#---------------------------------------
def print_key_value(day, num_run_outs, total_runouts, my_output_stream):

    # 1. I compute the percentage
    percentage = ((num_run_outs * 1.0) / (total_runouts * 1.0)) * 100.0

    # 2. We come up with the String to be printed
    my_str = day + '\t' + "(" + str(num_run_outs) + ", " + str(percentage) + ")" + '\n'

    # 3. I print it
    my_output_stream.write(my_str)

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    # 1. I unpack my_mapper_input_parameters
    total_runouts = my_reducer_input_parameters[0]

    # 2. I create 3 variables:

    # 2.1. One for the current day we are processing
    current_day = ""

    # 2.2. One for the number of runouts found for it
    current_num_runouts = 0

    # 2.3. I create a dictionary where I will add the days ordered from the one with highest run outs to the lowest
    res = {}

    # 3. I iterate through each line of the input file
    for line in my_input_stream:
        # 3.1. I get the info from the line
        (new_day, new_num_run_outs) = get_key_value(line)

        # 3.2. If I am dealing with a new day (key)
        if new_day != current_day:
            # 3.2.1. If it is not the first day I process, I update the number of runouts
            if current_day != "":
                res[current_day] = current_num_runouts

            # 3.2.2. I assign the current key to the new key I am starting processing
            current_day = new_day
            current_num_runouts = 0

        # 3.3. I update the num runouts
        current_num_runouts = current_num_runouts + new_num_run_outs

    # 4. I print the last day
    if current_day != "":
        res[current_day] = current_num_runouts

    # 5. I reverse the dictionary by the value
    my_sorted_dict = sorted(res, key=res.get, reverse=True)

    # 6. I write the result into the file
    for r in my_sorted_dict:
        day = r
        runouts = res[r]
        print_key_value(day, runouts, total_runouts, my_output_stream)

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
    input_file_example = "../../../my_result/A01 - Part2/SecondRound/my_sort_results.txt"
    output_file_example = "../../my_result/A01 - Part2/SecondRound/my_reducer_results.txt"

    # 3. my_reducer.py input parameters
    # We list the parameters here
    total_ran_outs = 1597

    # We create a list with them all
    my_reducer_input_parameters = [total_ran_outs]

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
           )
