#!/usr/bin/python3

'''
Prints the first x elements of a list that are intergers
Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns: The number of elements printed.
'''

def safe_print_list_integers(my_list=[], x=0):
	count = 0
	for element in range(x):
		try:
			print("{:d}".format(my_list[element], end="")
			count += 1
			if count == x:
				break
		except (ValueError, TypeError):
			continue
		print()
		return count
