dsaQ7:Left rotate array by K places

arr = [1,2,3,4,5]
k = 2
temp=arr[:k]
arr = arr[k:] + temp
print(arr)

output:
[3, 4, 5, 1, 2]

