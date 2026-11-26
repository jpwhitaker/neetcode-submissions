from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    int_1, int_2, int_3 = triplet
    return_sum = int_1 + int_2 + int_3
    return return_sum

def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    w, h, d = box_dimensions
    volume = w*h*d
    return volume
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
