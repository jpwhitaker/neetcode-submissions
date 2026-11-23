from typing import List

def read_integers() -> List[int]:
    user_string = input()
    user_list = user_string.split(',')
    return_list = []

    for item in user_list:
        return_list.append(int(item))

    return return_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
