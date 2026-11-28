from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    joined_array = arr1

    for i, num in enumerate(arr2):
        joined_array.append(num)

    return joined_array


def pop_n(arr: List[int], n: int) -> List[int]:
    
    if n > len(arr):
      return []

    for i in range(len(arr) - n, len(arr)):
        arr.pop()
    
    return arr


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    index = min(index, len(arr))
    
    arr.insert(index, element)

    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
