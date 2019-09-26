import getopt
import os
import sys


def main(argv):
    # Begin (source: https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
    input_type = ''
    try:
        opts, args = getopt.getopt(argv, "ht:", ["ntype="])
    except getopt.GetoptError:
        print('test.py -t <inputtype>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -t <inputtype>')
            sys.exit()
        elif opt in ("-t", "--ntype"):
            input_type = arg
    # End

    if input_type == '1' or input_type == '2' or input_type == '3' or input_type == '4':
        os.system(
            'echo `python3 generate_input_sort_comparison.py -n 5000 -s 6 -r 5000 -t {} -a 3 '
            '-o input_{}_sort_comparison.txt`'.format(input_type, input_type))
        os.system(
            'echo `python3 assignment_sort_comparison.py -i input_{}_sort_comparison.txt -a '
            '3 -o output_{}_sort_comparison.json`'.format(
                input_type,
                input_type))
        os.system(
            'echo `python3 plot_graph_sort_comparison.py -i output_{}_sort_comparison.json '
            '-t "Input Plot{}"`'.format(input_type, input_type))
    elif input_type == '5':
        os.system(
            'echo `python3 generate_input_sort_comparison.py -n 100000 -s 1 -r 50 -t {} -a 1 '
            '-o input_{}_sort_comparison.txt`'.format(input_type, input_type))
        os.system(
            'echo `python3 assignment_sort_comparison.py -i input_{}_sort_comparison.txt -a 1 '
            '-o output_{}_sort_comparison.json`'.format(
                input_type,
                input_type))
        os.system(
            'echo `python3 plot_graph_sort_comparison.py -i output_{}_sort_comparison.json '
            '-t "Input Plot{}"`'.format(input_type, input_type))


if __name__ == "__main__":
    main(sys.argv[1:])
