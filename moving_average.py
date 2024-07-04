n = int(input()) 
arr1 = list(map(int, input().split()))
win = int(input()) 
arr2=[]


for i in range(n-win+1):
    current_sum = sum(arr1[i:i+win])
    arr2.append(current_sum/win)

print(" ".join(str(x) for x in arr2))