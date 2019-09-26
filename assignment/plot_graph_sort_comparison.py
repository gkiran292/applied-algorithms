import getopt
import json
import sys
from typing import List

import pandas as pd
from matplotlib import pyplot
import sortinfo


# plt.plot(['Iteration1','Iteration2','Iteration3'], result)

# plt.ylabel('Execution Time')
# plt.title('Selection Sort - Input 5')
# plt.show()
def get_graph_plot_points(result: List[sortinfo.SortInfo], avg_required: str):
    out_dict_list = [x.to_dict() for x in result]
    # Reference (source: https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/)
    df_object = pd.DataFrame(out_dict_list)

    x_axis_data = []
    y_axis_dict = {}
    y_axis_label = []
    for input_n, group_n in df_object.groupby('input_n'):
        x_axis_data.append(input_n)
        for technique, group_tech in group_n.groupby('sort_technique'):
            y_axis_label.append(technique)
            if technique in y_axis_dict:
                if avg_required.upper() == 'TRUE':
                    y_axis_dict[technique].append(group_tech['time_in_secs'].mean())
                else:
                    y_axis_dict[technique].append(group_tech['time_in_secs'].sum())
            else:
                if avg_required.upper() == 'TRUE':
                    y_axis_dict[technique] = [group_tech['time_in_secs'].mean()]
                else:
                    y_axis_dict[technique] = [group_tech['time_in_secs'].sum()]
    return x_axis_data, y_axis_dict


def plot_comparison_graph(result: List[sortinfo.SortInfo], title: str, avg_required: str):
    x_axis_data, y_axis_dict = get_graph_plot_points(result, avg_required)

    x_axis_data = [str(x) for x in x_axis_data]
    for key in y_axis_dict:
        print("input_n: " + str(x_axis_data))
        print(key, ': ' + str(y_axis_dict[key]))
        pyplot.plot(x_axis_data, y_axis_dict[key], marker='o', label=key)

    pyplot.legend()
    pyplot.xlabel("Input n")
    pyplot.ylabel('Time of execution(secs)')
    pyplot.title(title)
    pyplot.savefig('{}.png'.format(title))


def main(argv):
    # Begin (source: https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
    input_file = ''
    title = ''
    avg_required = ''

    try:
        opts, args = getopt.getopt(argv, "hi:a:t:", ["ifile=", "avgr=", "title="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -a <avgrequired> -t <plottitle>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -a <avgrequired> -t <plottitle>')
            sys.exit()
        elif opt in ("-t", "--title"):
            title = arg
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-a", "--avgr"):
            avg_required = arg

    # End

    try:
        with open(input_file, "r") as f_in:
            result = sortinfo.sort_info_from_dict(json.load(f_in))
    finally:
        f_in.close()

    plot_comparison_graph(result, title, avg_required)


if __name__ == "__main__":
    main(sys.argv[1:])
