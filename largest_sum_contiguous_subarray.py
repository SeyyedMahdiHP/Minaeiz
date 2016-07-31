# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""
In computer science, the maximum subarray problem is the task of finding
the contiguous subarray within a one-dimensional array of numbers which has the largest sum.
 For example, for the sequence of values [-2, 1, -3, 4, -1, 2, 1, -5, 4];
  the contiguous subarray with the largest sum is 4, −1, 2, 1, with sum 6.
The problem was first posed by Ulf Grenander of Brown University in 1977,
as a simplified model for maximum likelihood estimation of patterns in digitized images.
 A linear time algorithm was found soon afterwards by Jay Kadane of Carnegie-Mellon University (Bentley 1984).
https://en.wikipedia.org/wiki/Maximum_subarray_problem
http://www.practice.geeksforgeeks.org/problem-page.php?pid=106
"""


def largest_sum_contigues_subarray(array_list):
    current_largest_subarray = final_largest_subarray = array_list[0]
    subarray_start_index = 0
    for i in range(1, len(array_list)):
        if (array_list[i] >= (current_largest_subarray + array_list[i])) and (array_list[i] >= final_largest_subarray):
            subarray_start_index = i
        current_largest_subarray = max(array_list[i], current_largest_subarray + array_list[i])
        final_largest_subarray = max(final_largest_subarray, current_largest_subarray)
    return [subarray_start_index, final_largest_subarray]


input_value = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # [2, 3, -1, -20, 5, 10]  #
print(largest_sum_contigues_subarray(input_value))
