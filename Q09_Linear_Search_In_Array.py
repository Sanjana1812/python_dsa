dsaQ9:Linear search in array

arr = [10,20,30,40,50]
target = 70
found= False
for i in arr:
  if i == target:
    print("found",target)
    found = True
    break
if found == False:
  print("not found",target)

output:
not found 70

