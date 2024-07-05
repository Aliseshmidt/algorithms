
unsort_arr = list(map(int, input().split()))

def shaker_sort(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        swaped = False
        for i in range(left, right):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaped = True
        right -= 1
        if swaped == False:
            break
        swaped = False
        for j in range(right, left, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swaped = True
        if swaped == False:
            break
        left += 1
    return arr

print(shaker_sort(unsort_arr))

## алгоритм работает быстрее, тк с каждой итерацией границы проверки массива уменьшаются ##
# Асимптотика в худшем случае - О(n^2)
# Асимптотика в лучшем случае - О(n) - потому что
# при одном проходе по массиву можно определить, отсортирован ли он. 
# Если массив уже отсортирован, то достаточно одного прохода без обменов, чтобы убедиться в этом.
