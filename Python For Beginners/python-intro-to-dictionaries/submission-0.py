from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    return_dict = {}
    return_dict[name] = age
    return return_dict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    return_dict = {}
    for i in range(len(words)):
        return_dict[words[i]] = i
    return return_dict



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
