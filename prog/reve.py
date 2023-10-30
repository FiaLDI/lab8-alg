#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


def buildMaxHepq(A):
    for i in range(len(A)//2, 1, -1):
        heapq._siftdown(A, 0, i)

def heapSort(A):
    print(A)
    buildMaxHepq(A)
    print(A)
    size = len(A) - 1
    for i in range(len(A) - 1, 2, -1):
        A[size], A[0] = A[0], A[size]
        size -= 1
        heapq._siftdown(A, 0, i)
    print(A)

if __name__ == "__main__":
    a = [4, 9, 7, 8, 6, 11, 12]
    heapSort(a)

    