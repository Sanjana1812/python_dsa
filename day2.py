num = int(input("enter a int num:"))
if num > 0:
  print("num is pos")
elif num <0 :
  print("num is neg")
else:
  print("num is zero")

  output:
enter a int num:0
num is zero
enter a int num:8
num is pos
enter a int num:-3
num is neg


num = int(input("enter a num:"))
if num % 2 == 0:
  print("num is even")
else:
  print("num is odd")

output:
enter a num:12
num is even
enter a num:7
num is odd
enter a num:0
num is even


age = int(input("enter a age:"))
if age >= 18:
  print("eligible for vote")
else:
  print("not eligible")

  output:
enter a age:17
not eligible

enter a age:18
eligible for vote

enter a age:25
eligible for vote

num = int(input("enter a num:"))
if num %5== 0 and num%11 == 0:
  print("num is divisible by 5 and 11")
else:
  print("num is not divisible by 5 and 11")

output:
enter a num:55
num is divisible by 5 and 11

enter a num:110
num is divisible by 5 and 11

enter a num:25
num is not divisible by 5 and 11

num1 = int(input("enter a num1:"))
num2 = int(input("enter a num2:"))
if num1 > num2:
  print(num1,"largest number")
elif num2> num1:
  print(num2,"Largest Number")
else:
  print("both are equal")

output:
enter a num1:4
enter a num2:9
9 Largest Number

enter a num1:6
enter a num2:6
both are equal


num1 = int(input("enter a num1:"))
num2 = int(input("enter a num2:"))
num3 = int(input("enter a num3:"))
if num1 > num2:
  print(num1,"largest number")
elif num2> num1:
  print(num2,"Largest Number")
elif num3> num2:
  print(num3,"Largest Number")
elif num3> num1:
  print(num3,"Largest Number")
else:
  print("all nums are equal")

output:
enter a num1:10
enter a num2:25
enter a num3:7
25 Largest Number

enter a num1:5
enter a num2:5
enter a num3:5
all nums are equal


marks = int(input("enter a marks:"))

if marks <0 or marks>100:
  print("invalid marks")
elif marks >=90:
  print("grade A")
elif marks >=75:
  print("grade B")
elif marks>=60:
  print("grade C")
elif marks>=40:
  print("grade D")
else:
  print("Fail")

output:
enter a marks:95
grade A

enter a marks:75
grade B

enter a marks:40
grade D

enter a marks:39
Fail

enter a marks:101
invalid marks


year= int(input("enter a year:"))
if (year%400==0) or (year%4 ==0 and year%100!=0):
  print("its a leap year")
else:
  print("it not a leap year")

output:
enter a year:2024
its a leap year

enter a year:1900
it not a leap year

enter a year:2000
its a leap year

  char = input("enter a char:")
if len(char) == 1 and char.isalpha():
  
  if char.lower() in ['a','e','i','o','u']:
    print("vowels")
  else:
    print("consonant")
else:
  print("invalid input")

  output:
enter a char:a
vowels

enter a char:Z
consonant

enter a char:7
invalid input

enter a char:ab
invalid input

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
  print(num1+num2)
elif op == "-":
  print(num1-num2)
elif op == "/":
  if num2 == 0:
    print("cant divide by 0")
  else:
    print(num1/num2)

output:
Enter first number: 8
Enter operator (+, -, *, /): +
Enter second number: 2
10.0

Enter first number: 8
Enter operator (+, -, *, /): /
Enter second number: 0
cant divide by 0

Enter first number: 8
Enter operator (+, -, *, /): %
Enter second number: 2

