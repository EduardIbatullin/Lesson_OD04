# O(n) - линейная сложность алгоритма


def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


array = [10, 20, 30, 40, 50]

print(line_search(array, 30))
print(line_search(array, 60))