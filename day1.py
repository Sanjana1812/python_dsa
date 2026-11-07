name = 'Sanjana'
age = 22
city ='Mysore'
programming_lang = 'Python'
print('Name :',name)
print('Age:',age)
print('City:',city)
print('Fav Programming Language:',programming_lang)

output :
Name : Sanjana
Age: 22
City: Mysore
Fav Programming Language: Python


a= 10
b = 20
print("Sum:",a +b)

output:
Sum: 30

a = int(input("Enter First Num:"))
b = int(input("Enter Second Num:"))
print("Multiply:", a *b)

Enter First Num:10
Enter Second Num:20
Multiply: 200

a = int(input("Enter a number :"))
square_root = a ** 0.5 
print("Square root of a num:",square_root)
cube_root = a ** (1/3)
print("Cube root of a num:",cube_root)

output:
Enter a number :5
Square root of a num: 2.23606797749979
Cube root of a num: 1.7099759466766968

c= float(input("Enter a temp:"))
f = (c*9/5 ) + 32
print("celisius is equals to fahrenheit:", f)


output:
Enter a temp:22
celisius is equals to fahrenheit: 71.6

a = int(input("enter a first num:"))
b = int(input("enter a second num:"))
print("floor division:", a // b)
print("remainder:", a % b )

output:
enter a first num:10
enter a second num:3
floor division: 3
remainder: 1

a = 10
b = 3
print(f"before swap: a = {a} , b = {b}")
a , b = b , a
print(f"after swap: a = {a} , b = {b}")

output:
before swap: a = 10 , b = 3
after swap: a = 3 , b = 10


age = int(input("enter dob year:"))
current_year= 2026
print("age:", age - current_year)

output:
enter dob year:2003
age: -23

number = int(input("enter a whole number:"))
is_divisible = ( number % 5 == 0)
print("number:", is_divisible)

output:
enter a whole number:5
number: True


marks1= int(input("enter a subject 1 marks:"))
marks2= int(input("enter a subject 2 marks:"))
marks3= float(input("enter a subject 3 marks:"))
total = marks1 + marks2 + marks3 
avg = total / 3
print("total:", total)
print("avg:", avg)

output:
enter a subject 1 marks:55
enter a subject 2 marks:99
enter a subject 3 marks:89.5
total: 243.5
avg: 81.16666666666667
