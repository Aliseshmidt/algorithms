n = int(input()) 
arr1 = list(map(int, input().split()))
win = int(input()) 
arr2=[]

def summ(arr, win, i):
    return sum(arr[i:i+win])


for i in range(n-win+1):
    arr2.append(summ(arr1, win, i)/win)

print(" ".join(str(x) for x in arr2))