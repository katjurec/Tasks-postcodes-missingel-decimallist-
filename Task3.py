# TASK 3

def print_list():
    int_list = [x for x in range(20, 60, 5)]
    decimal_list = []

    for element in int_list:
        decimal_list.append(element / 10.0)
    return decimal_list


print(print_list())
