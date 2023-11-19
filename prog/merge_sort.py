#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        m = len(arr) // 2
        left, inversion_left = merge_sort(arr[:m])
        right, inversion_right = merge_sort(arr[m:])
        merged, inversion_merge = merge(deque(left), deque(right))
        return merged, inversion_left + inversion_right + inversion_merge


def merge(left, right):
    merged = []
    inversion = 0
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.popleft())
        else:
            merged.append(right.popleft())
            inversion += len(left)
    merged.extend(left)
    merged.extend(right)
    return merged, inversion

if __name__ == '__main__':
    array = [8, 7, 3, 10, 1, 6, 4, 1, 9, 2, 11]
    print("Array =", array)
    _, inversion = merge_sort(array)
    print("Количество инверсий в массиве =", inversion)