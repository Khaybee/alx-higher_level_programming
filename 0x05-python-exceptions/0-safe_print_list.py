#!/usr/bin/python3

"""Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
"""

def safe_print_list(my_list=[], x=0):
	try:
		elements_printed = 0
		for i in my_list:
			if elements_printed < x:
				print(i, end="")
				elements_printed += 1
			else:
				break
		print()
		return (elements_printed)
	except IndexError:
		pass
