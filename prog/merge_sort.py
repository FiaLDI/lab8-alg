#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        m = len(arr) // 2
        left, inversion_left = merge_sort(arr[:m])
        right, inversion_right = merge_sort(arr[m:])
        merged, inversion_merge = merge(left, right)
        return merged, inversion_left + inversion_right + inversion_merge


def merge(left, right):
    merged = []
    inversion = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversion += len(left) - i
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, inversion


if __name__ == '__main__':
    array = [8, 7, 3, 10, 1, 6, 4, 1, 9, 2, 11]
    print("Array =", array)
    _, inversion = merge_sort(array)
    print("Количество инверсий в массиве =", inversion)
