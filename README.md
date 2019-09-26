# applied-algorithms #
## Generating input script ##
    
    python3 generate_input_sort_comparison.py -n 5000 -s 6 -r 5000 -t {} -a 3 -o input_1_sort_comparison.txt

1. n is the number used for input <br/>
2. s is the number by which n is increased by n times <br/> 
For example: iteration 1: n = 5000, iteration 2: n = 5000*2 ... upto iteration s <br/>
3. r is the range of random numbers that needs to be generated <br/>
4. t is the input type (input type is present in the document called assignment1.pdf)<br/>
5. a is the average number of inputs to be considered <br/>
For example: if a=3 and s=2 then, input size 5000 would be generated 3 times and input size 10000 would be generated 3 times <br/>
6. o is the output file name (which would eventually will be the input file for the algorithm execution program) <br/>

## Executing algorithm script ##
    
    python3 assignment_sort_comparison.py -i input_1_sort_comparison.txt -a 3 -s 'mqi' -o output_1_sort_comparison.json

1. a is the number of times a given sorting algorithm should execute (depends upon the average number 'a' that is provided in the input) <br/>
2. s is the type of sort to be executed on the input <br/>
    b - bubble sort <br/>
    s - selection sort <br/>
    i - insertion sort <br/>
    m - merge sort <br/>
    q - quick sort <br/>
3. i is the input file which the file generated using 'generating input' instructions <br/>
4. o is the output file for which is of type json (eventually this file would be input for the plot generation script) <br/>

## Executing plot generation script ##
    
    python3 plot_graph_sort_comparison.py -i output_1_sort_comparison.json -t "Input Plot 1"

1. i is the input file from the following 'algorithm execution' instructions <br/>
2. t is the title of the plot <br/>
3. a is the avg_required parameter where you should mention a = true or a = false for it to consider mean or the sum while plotting <br/>

NOTE: Change the file names according to the input numbers <br/>
For example: input_1..... for 1st input, input_2... for 2nd input and so on <br/>