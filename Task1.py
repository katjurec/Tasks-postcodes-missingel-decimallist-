# TASK 1

def split_codes(cd):
    splitted_value = cd.split("-")
    return splitted_value


def generate_codes(sc):
    gen_codes = []

    a = int(sc[0][0] + sc[0][1])
    b = int(sc[1][0] + sc[1][1])

    for n in range(b - a):
        gen_codes.append(a + n)

    gen_codes.append(b)
    output_codes = []

    for code in range(len(gen_codes)):
        to_split = str(gen_codes[code])
        output_codes.append(to_split[:2] + "-" + to_split[2:])

    return output_codes


first = input("Enter the limit values for the post codes\nFirst code:   ")
second = input("\nSecond code:   ")
splitted = [split_codes(first), split_codes(second)]
generated_codes = generate_codes(splitted)

print("The list of generated codes: \n")
for i in range(len(generated_codes)):
    print(generated_codes[i])
