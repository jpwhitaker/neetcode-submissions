def add_two_numbers() -> int:
    input_string = input()

    input_string_list = input_string.split(",")

    input_integers = []

    for item in input_string_list:
        input_integers.append(int(item))

    return (input_integers[0] + input_integers[1])



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
