def test(array, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and array[largest] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest == i:
        return
    else:
        array[i], array[largest] = array[largest], array[i]
        test(array, largest, n)

def heap_sort(array):
    lenght = len(array)
    for j in range((lenght // 2) - 1, -1, -1):
        test(array, j, lenght)
    for j in range(lenght - 1, 0, -1):
        array[0], array[j] = array[j], array[0]
        test(array, 0, j)
    return array

array = [1, 5, 59, 32, 452, 22, 234, 6, 7]
print(heap_sort(array))



