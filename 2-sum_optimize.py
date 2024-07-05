n = int(input())
arr = list(map(int, input().split()))
couple = int(input())
arr_couple = []

def find_couple(arr, couple, n):
    arr.sort()  
    left = 0
    right = len(arr) - 1 
    while left != right:
        current_sum = arr[left] + arr[right]
        if current_sum == couple:
            return arr[left], arr[right]
        if current_sum > couple:
            right -= 1
        else:
            left += 1

arr_couple = find_couple(arr, couple, n)
if not arr_couple:
    print(None)
else:
    print(" ".join(str(x) for x in arr_couple))
