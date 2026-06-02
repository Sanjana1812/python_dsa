dsaQ4:Check if array is sorted

arr = [1,2,3,4,5]
is_sorted = True
for i in range(len(arr)-1):
  if arr[i]> arr[i+1]:
    is_sorted = False
print("sorted array:",is_sorted)

output:
sorted array: True
