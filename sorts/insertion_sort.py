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

#https://res.cloudinary.com/practicaldev/image/fetch/s--Jb4_F3IM--/c_imagga_scale,f_auto,fl_progressive,h_420,q_66,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dikaizalparzhpkb5wxi.gif