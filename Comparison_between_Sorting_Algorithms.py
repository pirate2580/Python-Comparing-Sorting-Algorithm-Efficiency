# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:17:34 2020

@author: farhan
"""

import random
arr = list(range(1,101))
random.shuffle(arr)

def bubblesort(arr):
    bubblesort_comparisons = 0
    for i in range (0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            bubblesort_comparisons+=1
    return arr, bubblesort_comparisons
print ('BUBBLESORT', bubblesort(arr))

def insertionsort(arr):
    insertionsort_comparisons = 0
    for i in range (1,len(arr)):
        for j in range (i,-1,-1):
            if arr[j]>arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
            insertionsort_comparisons +=1
    return arr, insertionsort_comparisons
print ('INSERTIONSORT',insertionsort(arr))

def selectionsort(arr):
    selectionsort_comparisons = 0
    for i in range (0,len(arr)):
        for j in range (i+1,len(arr)-1):
            if arr[j]>arr[i]:
                i = j
                arr[j],arr[i] = arr[i], arr[j]
            selectionsort_comparisons +=1
    return arr, selectionsort_comparisons
print ('SELECTIONSORT',selectionsort(arr))

mergesort_comparisons = 0
def mergesort(arr):
    global mergesort_comparisons
    if len(arr)>1:
        leftside = arr[:len(arr)//2]
        rightside = arr[len(arr)//2:]
        leftside = mergesort(leftside)
        rightside = mergesort(rightside)
        arr = []
        #print (leftside, rightside)

        while len(leftside)>0 and len(rightside)>0:
            if leftside[0]<rightside[0]:
                arr.append(leftside[0])
                leftside.pop(0)
            else:
                arr.append(rightside[0])
                rightside.pop(0)
                print(arr)
            mergesort_comparisons +=1

        for i in leftside:
            arr.append (i)
            mergesort_comparisons +=1
        for i in rightside:
            arr.append (i)
            mergesort_comparisons +=1

    return arr
print('MERGESORT',mergesort(arr),mergesort_comparisons)

quicksort_comparisons = 0
def partition(arr, start, end):
    global quicksort_comparisons
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
         while low <= high and arr[high] >= pivot:
            high = high - 1
            quicksort_comparisons +=1
            
         while low <= high and arr[low] <= pivot:
            low = low + 1
            quicksort_comparisons +=1
            print(quicksort_comparisons)
            
         if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            quicksort_comparisons +=1
         else:
            
            break

    arr[start], arr[high] = arr[high], arr[start]

    return arr, high


def quicksort(arr, start, end):
    if start >= end:
        return
    arr, p = partition(arr, start, end)
    quicksort(arr, start, p-1)
    quicksort(arr, p+1, end)
quicksort(arr,0,len(arr)-1)
print('QUICKSORT',arr,quicksort_comparisons)

# A median-selection algorithm can be used to perform a selection algorithm or sorting algorithm, by selecting the median of the array as the pivot element in Quickselect or Quicksort algorithm