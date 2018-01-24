"""This module determines how long the light has been on.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #347 [Easy] How Long Has the Light Been On?
https://www.reddit.com/r/dailyprogrammer/comments/7qn07r/20180115_challenge_347_easy_how_long_has_the/

Submitted 1/23/2018
"""

sample_input = [[1, 3], [2, 3], [4, 5]]
input_1 = [[2, 4], [3, 6], [1, 3], [6, 8]]
input_2 = [[6, 8], [5, 8], [8, 9], [5, 7], [4, 7]]
bonus_input = [[15, 18], [13, 16], [9, 12], [3, 4], [17, 20], [9, 11], [17, 18],
               [4, 5], [5, 6], [4, 5], [5, 6], [13, 16], [2, 3], [15, 17], [13, 14]]

def interval_calc(times_list):
    """Determines length of next interval of lights on time and returns the original list with this interval removed.
    Takes a SORTED list of non-zero length. Each list item is to be a list of length 2 formatted as [entrance, exit]"""
    [enter, exit] = times_list.pop(0)
    last_index = None

    for index, time in enumerate(times_list):
        if time[0] <= exit:
            last_index = index
            if time[1] > exit:
                exit = time[1]

    interval = exit - enter
    if last_index is not None:
        return_list = times_list[last_index+1:]
    else:
        return_list = []


    return interval, return_list

curr_input = sample_input
curr_input.sort()
interval = 0


while len(curr_input) > 0:
    out_interval, curr_input = interval_calc(curr_input)
    interval += out_interval

print(interval)