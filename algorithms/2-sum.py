# нахождение пары двух чисел, дающих в сумме введенное число

n = int(input("Input quantity of numbers: "))
arr = list(map(int, input("Input array: ").split()))
couple = int(input("Input summary of couple: "))
arr_couple = []
def find_couple(arr, couple):
    for i in range(0, n):
        for j in range(1, n):
            if i != j:
                if arr[i] + arr[j] == couple:
                    return [arr[i], arr[j]]

arr_couple = find_couple(arr, couple)

if not arr_couple:
    print("No relevant couple of numbers: ", None)
else:
    print("Relevant couple of numbers: ", " ".join(str(x) for x in arr_couple))