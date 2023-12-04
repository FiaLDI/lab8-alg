#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge_sort(list_of_nums):
    if len(list_of_nums) <= 1:
        return list_of_nums, 0
    else:
        m = len(list_of_nums) // 2
        left, inversion_left = merge_sort(list_of_nums[:m])
        right, inversion_right = merge_sort(list_of_nums[m:])
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
    list_of_nums = [8, 7, 3, 10, 1, 6, 4, 1, 9, 2, 11]
    print("list_of_nums =", list_of_nums)
    _, inversion = merge_sort(list_of_nums)
    print("Количество инверсий в списке =", inversion)
