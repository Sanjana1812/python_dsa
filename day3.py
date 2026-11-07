for i in range(1,5):
  print(i)

op:
1
2
3
4

for i in range(2,11,2):
  print(i)

op:
2
4
6
8
10

count = 3
while count > 0:
    print(count)
    count -= 1
op:
3
2
1

for i in range(1,6):
  if i == 4:
    break
  print(i)

op:
1
2
3

for i in range(1,6):
  if i == 3:
    continue
  print(i)

op:
1
2
4
5

for i in range(1,11):
  print(i)

op:
1
2
3
4
5
6
7
8
9
10

for num in range(1,21):
  if num%2 == 0:
    print(num)

op:
2
4
6
8
10
12
14
16
18
20


n =5
total = 0
current = 1
while current <= n:
  total += current 
  current += 1
print(total)

op:
15

user_num = int(input("enter a num:"))
for num in range(1,11):
  print(user_num*num)

op:
enter a num:3
3
6
9
12
15
18
21
24
27
30

user_num = int(input("enter a num:"))
while user_num >0:
  print(user_num)
  user_num-=1
print("Go!")

op:
enter a num:3
3
2
1
Go!


secret= 7
user = int(input("enter a guess:"))
while user!= secret:
  print("guess again")
  user = int(input("enter a guess again:"))
print("correct")

op:
enter a guess:3
guess again
enter a guess again:4
guess again
enter a guess again:6
guess again
enter a guess again:7
correct


for i in range(1,11):
  if i == 7:
    break
  print(i)

op:
1
2
3
4
5
6

for i in range(1,21):
  if i%3==0:
    continue
  print(i)

op:

1
2
4
5
7
8
10
11
13
14
16
17
19
20

var = 1
n = int(input("enter a num:"))
for i in range(1,n+1):
  var*=1
print(var)

op:
enter a num:5
120


count = 0
n = int(input("enter a num:"))
while n>0:
  count+=1
  n//=10
print(count)

op:
enter a num:5832
4
