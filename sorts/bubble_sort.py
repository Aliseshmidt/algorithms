n = int(input())
unsort_arr = list(map(int, input().split()))

def bubble_sort(arr, n):
    i = 0
    while i < n-1:
        if arr[i+1] < arr[i]:
            curr = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = curr
            i = 0
        else:
            i +=1
    return arr

print(bubble_sort(unsort_arr, n))

# Асимптотика в худшем случае - О(n^2)
# Асимптотика в лучшем случае - О(n) - потому что
# при одном проходе по массиву можно определить, отсортирован ли он. 
# Если массив уже отсортирован, то достаточно одного прохода без обменов, чтобы убедиться в этом.
