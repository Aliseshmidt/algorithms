unsort_arr = list(map(int, input().split()))

def insertion_sort(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            curr = arr[i+1]
            for j in range()