import time
import random


def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
        swapped = True
    if not swapped:  # If no swaps occurred, the array is sorted
      break
  return arr


def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
  return arr


def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]  # Shift element
      j -= 1
    arr[j + 1] = key  # Insert at correct position
  return arr


def generate_test_case(size=10, max_value=100):
  return [random.randint(0, max_value) for _ in range(size)]


def benchmark_sorting():
  test_sizes = [100, 1000, 5000]
  algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
  }

  for size in test_sizes:
    test_data = generate_test_case(size)
    print(f"\nBenchmarking for array size {size}:")
    for name, sort_function in algorithms.items():
      data_copy = test_data.copy()
      start_time = time.time()
      sort_function(data_copy)
      elapsed_time = time.time() - start_time
      print(f"{name}: {elapsed_time:.6f} seconds")


# Running the benchmarking function
if __name__ == "__main__":
  benchmark_sorting()
