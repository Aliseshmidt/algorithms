# Метод скользящего среднего 
n = int(input()) 
arr1 = list(map(int, input().split()))
win = int(input()) 
arr2=[]

current_sum = sum(arr1[:win])
arr2.append(current_sum/win)

for i in range(1, n-win+1):
    current_sum = current_sum - arr1[i-1] + arr1[i + win - 1]
    arr2.append(current_sum/win)

print(" ".join(str(x) for x in arr2))