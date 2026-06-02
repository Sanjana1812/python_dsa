dsaQ4: Find the second largest element

arr = [10,20,30,40,50]
target=30
found = False
for i in arr:
  if i == target:
    print("Element found:",target)
    found= True
if found == False:
  print("not found")

output:
Element found: 30
