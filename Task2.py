# TASK 2

def print_missing_elements(inc, num):
    complete = list(range(1, num + 1))
    missing = []

    for x in range(len(inc)):
        inc[x] = int(inc[x])

    for element in complete:
        if element not in inc:
            missing.append(element)

    return print(missing)


def split_input(in_list):
    inc = in_list[0]
    num = int(in_list[1])

    inc = inc.replace("[", "")
    inc = inc.replace("]", "")
    inc = inc.split(",")
    return inc, num


input_list = input("Please enter the input list and nb. of elements i.e. \n[2,3,7,4,9], 10 :    ").split(", ")
incomplete, n = split_input(input_list)
print_missing_elements(incomplete, n)
