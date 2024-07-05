unsort_arr = list(map(int, input().split()))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(i, j , arr)
        arr[j + 1] = key
        print(arr)
    return arr

print(insertion_sort(unsort_arr))