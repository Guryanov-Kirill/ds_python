import random
from heap_sort import heap_sort


def test_unit():
    array = [1, 5, 59, 32, -452, 22, 234, 6, 7]
    assert heap_sort(array) == [-452, 1, 5, 6, 7, 22, 32, 59, 234]

def test_kritical():
    array1 = [1]
    assert heap_sort(array1) == [1]

    array2 = [5, 4, 3, 2, 1]
    assert heap_sort(array2) == [1, 2, 3, 4, 5]

    array3 = [2, 5, 67, 3, 5, 7, 54, 67]
    assert heap_sort(array3) == [2, 3, 5, 5, 7, 54, 67, 67]


def test_property_based():
    array4 = [random.randint(-100, 0) for i in range(10)]
    assert heap_sort(array4) == sorted(array4)

    array5 = [i for i in range(1000, -1000, -1)]
    assert heap_sort(array5) == sorted(array5)



