from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    top_score= None
    top_student= None
    for name, score in scores:
        if top_score == None or score > top_score:
            top_score = score
            top_student = name
    return top_student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
