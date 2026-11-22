def remove_fourth_character(word: str) -> str:
    new_start = word[:3]
    new_end = word[4:]
    return new_start + new_end

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
