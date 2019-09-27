import getopt
import json
import sys
import timeit
import sortinfo as si


def swap(arr, i1, i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# selection sort technique (source: https://www.geeksforgeeks.org/selection-sort/)
def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] <= nums[min_index]:
                min_index = j
        swap(nums, i, min_index)


# insertion sort technique (source: https://www.geeksforgeeks.org/insertion-sort/)
def insertion_sort(nums):
    for i in range(1, len(nums)):
        min_element = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > min_element:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = min_element


def merge_sort(nums):
    start = 0
    end = len(nums) - 1
    merge_sort_util(nums, start, end)


def merge_sort_util(nums, start, end):
    if start >= end:
        return

    mid = int((start + end) / 2)

    merge_sort_util(nums, start, mid)
    merge_sort_util(nums, mid + 1, end)
    merge_util(nums, start, mid, end)


def merge_util(nums, start, mid, end):
    temp_nums = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            temp_nums.append(nums[i])
            i += 1
        else:
            temp_nums.append(nums[j])
            j += 1

    index = i
    while index <= mid:
        temp_nums.append(nums[index])
        index += 1

    index = j
    while index <= end:
        temp_nums.append(nums[index])
        index += 1

    for index in range(0, len(temp_nums)):
        nums[start + index] = temp_nums[index]


def quick_sort(nums):
    start = 0
    end = len(nums) - 1

    quick_sort_util(nums, start, end)


def quick_sort_util(nums, start, end):
    if start >= end:
        return

    # Pivot is not passed to the function as it's deterministic Quick Sort as pivot is always the end
    partition_point = partition(nums, start, end)
    quick_sort_util(nums, start, partition_point - 1)
    quick_sort_util(nums, partition_point + 1, end)


def partition(nums, start, end) -> int:
    p_index = start
    if start == end:
        return p_index

    for i in range(start, end):
        if nums[i] <= nums[end]:
            nums[i], nums[p_index] = nums[p_index], nums[i]
            p_index += 1
    nums[p_index], nums[end] = nums[end], nums[p_index]
    return p_index


def store_sort_result(nums, sort_technique, iteration_number, input_n, output_lst):
    start_time = timeit.default_timer()
    sort_technique(nums)
    end_time = timeit.default_timer()

    print('sort_technique: ', sort_technique.__name__, ' iteration_number: ', iteration_number, ' input_n: ', input_n,
          ' time_in_secs: ', end_time - start_time)

    # result = si.sort_info_to_dict(si.SortInfo(sort_technique.__name__, iteration_number, input_n,
    #                         round(end_time - start_time, 2), nums))
    output_lst.append(si.SortInfo(sort_technique.__name__, iteration_number, input_n,
                                  end_time - start_time, nums))


def main(argv):
    # Begin (source: https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
    input_file = ''
    output_file = ''
    sort_types = ''
    average_number = ''
    try:
        opts, args = getopt.getopt(argv, "hi:a:s:o:", ["ifile=", "avgn=", "stype", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -a <avgnumber> -s <sorttypes> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -a <avgnumber> -s <sorttypes> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-a", "--avgn"):
            average_number = arg
        elif opt in ("-s", "--stype"):
            sort_types = arg
    # End

    try:
        with open(input_file, "r") as f_in:
            lines = json.load(f_in)
    finally:
        f_in.close()

    output_lst = []

    # To prevent the stack overflow in the worst case of quick sort
    sys.setrecursionlimit(31000)

    sort_set = set(sort_types)

    for i in range(0, len(lines), int(average_number)):
        for k in range(0, int(average_number)):
            if 'b' in sort_set:
                nums_bubble_sort = lines[i + k].copy()
                store_sort_result(nums_bubble_sort, bubble_sort, k + 1, len(nums_bubble_sort), output_lst)

            if 's' in sort_set:
                nums_select_sort = lines[i + k].copy()
                store_sort_result(nums_select_sort, selection_sort, k + 1, len(nums_select_sort), output_lst)

            if 'i' in sort_set:
                nums_insert_sort = lines[i + k].copy()
                store_sort_result(nums_insert_sort, insertion_sort, k + 1, len(nums_insert_sort), output_lst)

            if 'm' in sort_set:
                nums_merge_sort = lines[i + k].copy()
                store_sort_result(nums_merge_sort, merge_sort, k + 1, len(nums_merge_sort), output_lst)

            if 'q' in sort_set:
                nums_quick_sort = lines[i + k].copy()
                store_sort_result(nums_quick_sort, quick_sort, k + 1, len(nums_quick_sort), output_lst)

    try:
        with open(output_file, "w") as f_out:
            json.dump(si.sort_info_to_dict(output_lst), f_out, indent=4)
    finally:
        f_out.close()


if __name__ == "__main__":
    main(sys.argv[1:])
