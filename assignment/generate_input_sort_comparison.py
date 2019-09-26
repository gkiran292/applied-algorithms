import getopt
import sys
from random import randrange
import json

ASCENDING_INPUT = 'ASC'
DESCENDING_INPUT = 'DESC'
NOISY_ASCENDING_INPUT = 'N_ASC'
CONST_LENGTH_INPUT = 'CONST_INPUT'


def iterative_inputs(average_number, input_nums, input_number, rand_range, sort_type=''):
    for j in range(0, average_number):
        nums = [randrange(0, rand_range) for _ in range(0, input_number)]
        if sort_type == ASCENDING_INPUT:
            nums.sort()
        elif sort_type == DESCENDING_INPUT:
            nums.sort(reverse=True)
        elif sort_type == NOISY_ASCENDING_INPUT:
            nums.sort()
            for k in range(0, 50):
                first_number = randrange(0, input_number)
                second_number = randrange(0, input_number)

                nums[first_number], nums[second_number] = nums[second_number], nums[first_number]

        input_nums.append(nums.copy())


def generate_input(average_number, input_nums, input_number, rand_range, step_number, sort_input_type=''):
    for i in range(0, step_number):
        if sort_input_type == CONST_LENGTH_INPUT:
            iterative_inputs(average_number, input_nums, input_number, rand_range)
        else:
            iterative_inputs(average_number, input_nums, (i + 1) * input_number, (i + 1) * rand_range, sort_input_type)


def main(argv):
    # Begin (source: https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
    output_file = ''
    input_number = ''
    input_type = ''
    average_number = ''
    rand_range = ''
    step = ''
    try:
        opts, args = getopt.getopt(argv, "hn:o:t:r:a:s:", ["inumber=", "ofile=", "ntype=", "rrange=", "avgn=", "step="])
    except getopt.GetoptError:
        print('test.py -n <inputnumber> -s <numberofsteps> -r <randrange> -t <inputtype>, -a <averagenumber> -o '
              '<outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -n <inputnumber> -s <numberofsteps> -r <randrange> -t <inputtype>, -a <averagenumber> -o '
                  '<outputfile>')
            sys.exit()
        elif opt in ("-n", "--inumber"):
            input_number = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-t", "--ntype"):
            input_type = arg
        elif opt in ("-a", "--avgn"):
            average_number = arg
        elif opt in ("-r", "--rrange"):
            rand_range = arg
        elif opt in ("-s", "--step"):
            step = arg
    # End
    input_nums = []
    input_number = int(input_number)
    average_number = int(average_number)
    rand_range = int(rand_range)
    step = int(step)

    if input_type == '1':
        generate_input(average_number, input_nums, input_number, rand_range, step)
    elif input_type == '2':
        generate_input(average_number, input_nums, input_number, rand_range, step, ASCENDING_INPUT)
    elif input_type == '3':
        generate_input(average_number, input_nums, input_number, rand_range, step, DESCENDING_INPUT)
    elif input_type == '4':
        generate_input(average_number, input_nums, input_number, rand_range, step, NOISY_ASCENDING_INPUT)
    else:
        generate_input(average_number, input_nums, input_number, rand_range, step, CONST_LENGTH_INPUT)

    try:
        with open(output_file, "w") as f_out:
            json.dump(input_nums, f_out)
    finally:
        f_out.close()


if __name__ == "__main__":
    main(sys.argv[1:])
