
def remove_occurrences(lst: list[int], num: int) -> list[int]:
    return [x for x in lst if x != num]
list=[1, 2, 3, 4, 2, 5, 2]