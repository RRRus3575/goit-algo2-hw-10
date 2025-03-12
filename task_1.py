import random

def randomized_quick_sort(arr):
    """Рандомізоване швидке сортування"""
    if len(arr) < 2:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    """Детерміноване швидке сортування"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def generate_random_array(size, min_val=-10**6, max_val=10**6):
    """Генерація випадкових масивів"""
    return [random.randint(min_val, max_val) for _ in range(size)]


sizes = [10_000, 50_000, 100_000, 500_000]
arrays = {size: generate_random_array(size) for size in sizes}


randomized_quick_sort_arr = randomized_quick_sort(arrays[10_000])
print("Відсортований масив рандомізований:", randomized_quick_sort_arr)

randomized_quick_sort_arr2 = randomized_quick_sort(arrays[50_000])
print("Відсортований масив рандомізований:", randomized_quick_sort_arr2)

randomized_quick_sort_arr2 = randomized_quick_sort(arrays[100_000])
print("Відсортований масив рандомізований:", randomized_quick_sort_arr2)

randomized_quick_sort_arr2 = randomized_quick_sort(arrays[500_000])
print("Відсортований масив рандомізований:", randomized_quick_sort_arr2)


deterministic_quick_sort_arr = deterministic_quick_sort(arrays[10_000])
print("Відсортований масив детермінований:", deterministic_quick_sort_arr)

deterministic_quick_sort_arr2 = randomized_quick_sort(arrays[50_000])
print("Відсортований масив детермінований:", deterministic_quick_sort_arr2)

deterministic_quick_sort_arr2 = randomized_quick_sort(arrays[100_000])
print("Відсортований масив детермінований:", deterministic_quick_sort_arr2)

deterministic_quick_sort_arr2 = randomized_quick_sort(arrays[500_000])
print("Відсортований масив детермінований:", deterministic_quick_sort_arr2)
