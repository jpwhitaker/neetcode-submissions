from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    return_dict = {}

    
    for letter in word:
        if letter in return_dict:
            return_dict[letter] = return_dict[letter] + 1
        else:
            return_dict[letter] = 1
    
    return return_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
