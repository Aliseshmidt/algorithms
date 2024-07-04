n = int(input())
arr = list(map(int, input().split()))
couple = int(input())
arr_couple = []
def find_couple(arr, couple):
    for i in range(0, n):
        for j in range(1, n):
            if i != j:
                if arr[i] + arr[j] == couple:
                    return [arr[i], arr[j]]

arr_couple = find_couple(arr, couple)

if not arr_couple:
    print(None)
else:
    print(" ".join(str(x) for x in arr_couple))