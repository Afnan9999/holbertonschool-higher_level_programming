#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element two lists up to list_length.
    
    Args:
        my_list_1 (list): First list
        my_list_2 (list): Second list
        list_length (int): Number of elements to divide
    
    Returns:
        list: List of division results
    """
    result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result.append(div)
    return result
