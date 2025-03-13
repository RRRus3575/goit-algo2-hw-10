import random
import timeit
import matplotlib.pyplot as plt
from tqdm import tqdm


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

times_randomized = {}
times_deterministic = {}
repeat = 5

for size, array in tqdm(arrays.items(), desc="Вимірювання часу виконання"):
    time_randomized_quick_sort =  sum(timeit.repeat(lambda: randomized_quick_sort(array.copy()), repeat=repeat, number=1))/repeat
    time_deterministic_quick_sort =  sum(timeit.repeat(lambda: deterministic_quick_sort(array.copy()), repeat=repeat, number=1))/repeat
    times_randomized[size] = time_randomized_quick_sort
    times_deterministic[size] = time_deterministic_quick_sort
    

# Вивід результатів у термінал
print("\n=== Результати виконання сортувань ===\n")
for size in sizes:
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {times_randomized[size]:.4f} секунд")
    print(f"   Детермінований QuickSort: {times_deterministic[size]:.4f} секунд")
    print()  


# Побудова графіка
plt.figure(figsize=(10, 6))

plt.plot(sizes, [times_randomized[size] for size in sizes], marker="o", linestyle="-", label="Рандомізований QuickSort")
plt.plot(sizes, [times_deterministic[size] for size in sizes], marker="x", linestyle="-", label="Детермінований QuickSort")

plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.grid()

plt.show()