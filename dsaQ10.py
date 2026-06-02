dsaQ10:Find union of two sorted arrays

arr1=[1,2,3]
arr2=[2,3,4]

new_arr = []

for i in arr1+arr2:
  if i not in new_arr:
    new_arr.append(i)
print("Union:",new_arr)


output:
Union: [1, 2, 3, 4]


