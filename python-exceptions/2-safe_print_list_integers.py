#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers of a list.

    Args:
        my_list (list): List containing any type of elements.
        x (int): Number of elements to access in my_list.

    Returns:
        int: The number of integers successfully printed.
    """
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                continue
    except IndexError:
        pass
    print()
    return count
