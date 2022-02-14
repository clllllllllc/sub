from typing import NewType

SortedArray = NewType("Sorted Array", list)


def linear_search(arr: list, n):
    for i, val in enumerate(arr):
        if val == n:
            return i
    return False


def binary_search(arr: SortedArray, x):
    i1 = 0
    i2 = len(arr) - 1
    while i1 <= i2:
        mid = int((i2 + i1) // 2)
        if x == arr[mid]:
            return mid
        elif x < mid:
            i2 = mid - 1
        elif x > mid:
            i1 = mid + 1

    return False


def interval_search(x: str, y: str) -> list:
    leny = len(y) - 1
    for i in range(len(x) - leny):
        z = ''
        for j in range(leny + 1):
            z += x[i + j]
        if z == y:
            return[i, i + 1]
