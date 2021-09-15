#arr is array of (val, key) pairs
import math
import time
import random
import matplotlib.pyplot as plt


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(arr, univsize):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

# Returns max number of digits
def maxDigits(dec, b):
    cnt = 0
    while dec // b > 0:
        cnt += 1
        dec = dec // b
    cnt += 1
    return cnt

# Returns key-item pair:
# key = length of queue of digits of base b representation of dec.
# item = queue of digits of base b representation of dec.
def baseChange(dec, b, n):
    q = []
    while dec // b > 0:
        q.append(dec % b)
        dec = dec // b
    q.append(dec % b)
    while len(q) < n:
        q.append(0)
    return q

def radixSort(arr, n, univsize, b):
    digArr = [None] * n
    csArr = [None] * n
    # initialize countSort pre-processed array with key-item
    # pairs from arr
    for i in range(n):
        csArr[i] = [0, arr[i]]
        digArr[i] = maxDigits(arr[i][0], b)
    # base change
    digits = max(digArr)
    for i in range(n):
        bRep = baseChange(arr[i][0], b, digits)
        digArr[i] = [bRep[0], bRep]
    for j in range(digits):
        for i in range(n):
            csArr[i][0] = digArr[i][1][j]
            digArr[i][0] = digArr[i][1][j]
        csArr = countSort(csArr, b)
        digArr = countSort(digArr, b)
    for i in range(n):
        arr[i] = csArr[i][1]
    return arr

# unit testing
arr1 = [(1, 'a'), (2, 'b'), (4, 'c'), (8, 'd'), (3, 'e'), (16, 'f'), (2, 'g')]
assert(radixSort(arr1, 7, 20, 2) == [(1, 'a'), (2, 'b'), (2, 'g'), (3, 'e'),
(4, 'c'), (8, 'd'), (16, 'f')])

arr0 = [(11, "cat"), (14, "dog"), (2, "elephant"), (1432, "sealion")]
assert(radixSort(arr0, 4, 1500, 10) ==
[(2, "elephant"), (11, "cat"), (14, "dog"), (1432, "sealion")])

def test(arr):
    for i in range(len(arr) - 1):
        if arr[i][0] > arr[i+1][0]:
            return "Fail"
        return "Pass"

# 2C EXPERIMENTS

def exp():
    for powU in range(20, 21): # U = 2^powU
        for powN in range(1, 21): # n = 2^powN
            # 10 trials per value of n and U
            for t in range(4):
                # Generate array of length n where keys are drawn
                # uniformly and independently from [U]
                arr = []
                cAvgSum = rAvgSum = mAvgSum = 0
                for i in range(2**powN):
                    key = random.randrange(0, 2**powU)
                    item = random.random() # arbitrary item
                    arr.append((key, item))

                # 3 copies
                arr1 = [None] * 2**powN
                arr2 = [None] * 2**powN
                for i in range(2**powN):
                    arr1[i] = arr[i]
                    arr2[i] = arr[i]

                # Counting Sort
                cStart = time.time()
                cSorted = countSort(arr, 2**powU)
                cEnd = time.time()
                cRuntime = cEnd - cStart
                cAvgSum += cRuntime
                print("Count: U = 2^(" + str(powU) + "), n = 2^(" + str(powN) +
                "), Trial " + str(t) + ": " + "Runtime = " + str(cRuntime) +
                " Sorted: " + test(cSorted))

                # Radix Sort
                rStart = time.time()
                rSorted = radixSort(arr1, 2**powN, 2**powU, 2**powN)
                rEnd = time.time()
                rRuntime = rEnd - rStart
                rAvgSum += rRuntime
                print("Radix: U = 2^(" + str(powU) + "), n = 2^(" + str(powN) +
                "), Trial " + str(t) + ": " + "Runtime = " + str(rRuntime) +
                " Sorted: " + test(rSorted))

                # Merge Sort
                mStart = time.time()
                mSorted = mergeSort(arr2)
                mEnd = time.time()
                mRuntime = mEnd - mStart
                mAvgSum += mRuntime
                print("Merge: U = 2^(" + str(powU) + "), n = 2^(" + str(powN) +
                "), Trial " + str(t) + ": " + "Runtime = " + str(mRuntime) +
                " Sorted: " + test(mSorted))

            cAvg = cAvgSum / 4
            rAvg = rAvgSum / 4
            mAvg = mAvgSum / 4
            print("***********************************************************")
            print("Count: U = 2^(" + str(powU) + "), n = 2^(" + str(powN) +
            "), Expected Runtime = " + str(cAvg))
            print("Radix: U = 2^(" + str(powU) + "), n = 2^(" + str(powN) +
            "), Expected Runtime = " + str(rAvg))
            print("Merge: U = 2^(" + str(powU) + "), n = 2^(" + str(powN) +
            "), Expected Runtime = " + str(mAvg))
            print("***********************************************************")

        fig = plt.figure(figsize=(10,8))
        plt.rc('axes', titlesize=24)
        plt.title("Sorting Algorithms Runtime")
        count = plt.scatter(1, 1, color="maroon")
        radix = plt.scatter(1.1, 1.1, color="blue")
        merge = plt.scatter(1.2, 1.2, color="black")
        plt.legend([count, radix, merge], ['Countsort', 'Radixsort', 'Mergesort'])
        plt.show()
        # Code to save image file (to include in typeset submission)
        # fig.savefig(f"path/to/filename.png")

exp()
                #
