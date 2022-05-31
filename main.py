import math
import statistics
import random
import pickle
import csv

'''Python Class
24/06/2021

1st Token: Variables/Identifiers

1. Underscore is allowed to name variables.

2. Numbers are allowed but not as the first character.

3. Any special character except underscore is not allowed.

2nd Token: Keywords

These are words which contain special meaning in Python.

3rd Token: Literals

These are constant values which do not change.

10 is a numeric literal

Assignment Operator

x7 → Identifier, = → Assignment Operator, 10 → Literal

Single Assignement, single data value

This concept is called Loosely Binded/Coupled Datatype"

DocString is used to create documentation in a program.

Int conversion can only be done if input is a number.

int, float, str functions are called type casting. When the programmer converts one datatype into another.
Explicitly or manually: Conversion done by programmer, data loss may occur, may convert from smaller to bigger datatype or vice-versa
Implicitly: Conversion done by interpreter itself, data loss never occurs, always converts from small er bigger datatype

When you try to operate incompatible dataypes, error occurs because we did not do explicit conversion and implicit conversion cannot occur in incompatible datatypes.

None is a variable which has no value, null.

L Value - LHS, defined already
R Value - RHS, defined by user

To swap 2 values: a,b = b,a

Python Class
28/06/2021

#\n → New line is added to the print output


print("Hello world.", end=" ")
print("Hello world2.")

End is a parameter of print function.
Whatever we write inside the end quotes, it is printed between the statements.

OPERATORS:
1. Arithmetic Operators: +,-,*,/,,%, // (floor division)


Floor division gives quotient only, mod gives remainder only.

x = 15//2
print(x)
print(type(x))

y = 15/2
print(y)
print(type(y))

Parentheses Exponentiation Division Multiplication Addition Subtraction - PEDMAS

2. Relational Operators: <,>‚>=, !=, <=, ==

= is an assignment operator, while == is a relational operator
= assigns the value, == checks whether the equality is true or not.

x = 10
y = 20
print(x==y) Output → False

x = "abcd"
y = "pqrs"

print(x<y) True: Because ASCII value of a < p

x = "abcd"
y = "abce"
print(x>y)
print(x<y)

3. Logical Operators: and - multiplication, or - addition, not

First not, then and, last or.

4. Identity Operator: is

Q. Evaulate 7*(8/(5//2)) → 7*(8/2) → 7*4 → 28.0

Q. 3*32 → 27*2 → 729 (Wrong)
Exponentiation Operator is evaluated from right, if used multiple times: 3*32 → 3*9 → 19683

Q. (3*3)*2 → 729

These rules are called Operator Associativity.

Q. Output:
 x, z = 5, 10
 y = x + 3
 x = x - 1
 x = x + z
print(x,y,z)

y = 5 + 3 = 8
x = 5 - 1 = 4
x = 4 + 10 = 14, y = 8, z = 10

Q. print(14//4, 14%4, 14/4) → 3 2 3.5

Python Class
29/06/2021


a = 6
a < 5 and a < 10

a = 6
not(a < 5 and a < 10)
7 and 0
7 and 9
7 or 9
0 and 6
print(5 and 7 and 0)
print(0 or 5 or 7)→ 0 is false, so next: 5 is true, so it stops here

Identity Operator: is (if both variables point to the same memory location, is not

print(a == c)

True, because they both point to the same memory location.

id function: Tells the memory location of a variable.

print(hex(id(a)))
print(hex(id(c)))
print(a is c)
print(a == b)
print(a is b)

3 conditions when is doesn't work like ==:
1. Complex Numbers:

a = 10.2
b = 10.2

print(a == b)

print(a is b)

print(0.1 + 0.1 + 0.1 == 0.3)
print(0.1 + 0.1 + 0.1)
print(0.1000000000000000001 + 0.100000000000000 + 0.100000000000000)

d = "Gautam"

print('a' in d)
print('A' in d)

ASCII value of a and A are different
Augmented Assignment Operator aka Shorthand Assignment Operator:

a = a + b
a += b

a -= b

Bitwise Operators:

& - and operator
| - or operator
~ - not operator

a = 10
b = 12


1010
1100

&
1000

|
1110

~
0101
0011


print(a&b)
print(a|b)
print(~a)
print(~b)

c = 1010
d = 1100

print(c&d)

Q. not(10<20) and not(10>30)
A. False and True → False

Q. (6 == 3) and (4 == 4)
A. False

Q. (6<9) and (4>2)
A. True

Q.
x = 2
1 < x < 3
A. True

Python Class
30/06/2021


Q. Write a single-statement to:
1. Assign value 10 to

Aditya, [21.07.21 19:59]
[Forwarded from Gautam Prasanna Kappagal]
5 variables.
A. a = b = c = d = e = 10

2. Assign values 11, 12, 13 to 3 different variables.
A. a, b, c = 11, 12, 13

3. Print 3 words "one", "two", "three" on 3 different lines.
A. print("one", "two", "three", sep="\n")

Q. x = 10, y = 30
print(x, y, x+y, sep='&')
A. 10&30&40

Q.
x, y = 20, 30
x = y + 2
y = x - 2
print(x, y)

Q.
a,b,c = 11,22,33
a,b,c = a + 1, b - 2, c + 3
print(a,b,c)

Q. Find the error:
x = float(input("Age: "))
If the user enters 45.5.5

Q.
x = int(input("Age = "))
If user enters "abc", "type incompatibility error" is displayed.

Q.
str = 'it's her choice'

Q.
str = 'value"

Q.
x = y + 3

Q. Which out of the following are invalid identifiers?
1. 8rec, finally, rec_8, word.problem, a1b2, prec%, yes, not, nonlocal, i123

b = 6
a = 3
c = 4
d = 2
print((((a+b)>c) and ((b-c)<d)) or ((b+d)>=(a+c)))

Q.
Write a program to input the cost price of an item. Print the selling price if profit is 10% of the CP.

A. CP = float(input("Enter the cost price: "))
SP = 1.1*CP
print(str(SP))

Q. Write a program to input an angle in degrees and convert it into radians

deg = float(input("Enter the angle in degrees: "))
rad = math.pi/180*deg
print(str(rad))

STATEMENTS: Inputs provided by the user to perform certain tasks.

1. Empty statements: Doesn't perform any action, ex: pass (no action)
2. Single statements: Simply single statement, ex: x = 10
3. Compound statements: Combined single statements, ex. x = 10 y = 20 print(x+y)

Python Class
01/07/2021

FLOW OF EXECUTION:
1. Sequential flow (by default)
2. Conditional flow - if, else, elif
3. Iterative flow - for, while


Python Class
05/07/2021

mar = float(input("Enter marks: "))
if mar >= 90:
    print("Your grade is A.")

elif 80 < mar < 90:
    print("Your grade is B.")

elif 70 < mar < 80:
    print("Your grade is C.")

elif 60 < mar < 70:
    print("Your grade is D.")

elif 50 < mar < 60:
    print("Your grade is E.")

elif 40 < mar < 50:
    print("Your grade is F.")

x = int(input("Input int1: "))
y = int(input("Input int2: "))
z = int(input("Input int3: "))

S1 = x + y + z
print(S1)

if x == y != z:
    S2 = z + x
elif x == y == z:
    S2 = x
elif y == z != x:
    S2 = x + y
elif z == x != y:
    S2 = y + x
else:
    S2 = S1
print(S2)

Python Class
06/07/2021


a=int(input("enter num1"))
b=int(input("enter num2"))
c=int(input("enter num3"))
sum=a+b+c
print("sum is ",sum )
if a==b:
    print(a+b)
elif b==c:
    print(a+b)
elif a==c:
    print(b+c)

Q. Write a program to test the divisibility of a number with another number.
A.
x = int(input("Enter the number whose divisibility is to be checked: "))
y = int(input("Enter the number by which the first number is to be divided: "))

if x%y == 0:
    print("The first number is divisible by the second number.")
else:
    print("The first number is not divisible by the second number.")

Q. Write a program to display a menu for calculating area of a circle or perimeter of a circle.
A.

rad = int(input("Enter the radius of the circle: "))
area = math.pi*(rad**2)
cir = 2*math.pi*rad

choice = input("Enter 1 to find area, 2 to find perimeter: ")

if choice == "1":
    print("The area is", area, ".")
elif choice == "2":
    print("The perimeter is", cir, ".")
elif choice != "1" or choice != "2":
    print("Error! Enter only 1 or 2.")


Q. Write a program that reads 2 numbers and an arithmetic operator and display the computed result.
A.

x = float(input("Enter num1: "))
y = float(input("Enter num2: "))
z = input("Enter operator out of '+', '-', '/', '*', '//', '' or '%' only: ")

if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "/":
    print(x/y)
elif z == "*":
    print(x*y)
elif z == "%":
    print(x%y)
elif z == "":
    print(x**y)
elif z == "//":
    print(x//y)
else:
    print("Error! Enter only '+', '-', '/', '*', '', '//' or '%'!")

Python Class
07/07/2021

Q. Write a program to input a six digit number and divide it into 3 2 digit numbers.
A. 
x = int(input("Enter 6 digit number: "))
if len(str(x)) == 6:
    y1 = x//10000
    x2 = x%10000
    y2 = x2//100
    y3 = x%100

Aditya, [21.07.21 19:59]
[Forwarded from Gautam Prasanna Kappagal]
print(y1, y2, y3)
else:
    print("Enter only a 6 digit number.")

Q. Write a program to calculate and print the sum of even and odd integers of the first n natural numbers.
A. 

n = int(input("Enter limit of numbers: "))
if n%2 == 0:
    e = int(n*(n+2)/4)
    o = int((n/2)2)
    print("Even number sum is: ", e)
    print("Odd number sum is: ", o)
elif n%2 == 1:
    e = int((n**2 - 1)/4)
    o = int(((n+1)/2)**2)
    print("Even number sum is: ", e)
    print("Odd number sum is: ", o)
else:
    print("Enter only an integer.")

max=int(input("please enter the maximum value: "))
even=0
odd=0
for num in range(1,max+1):
    if (num%2==0):
        even=even+num
    else:
        odd=odd+num
print("The sum of Even numbers 1 to {0} = {1}".format(num,even))
print("The sum of odd numbers 1 to {0} = {1}".format(num,odd))

Python Class
08/07/2021

WHILE LOOP:
1. Set a variable value (Initialize the variable)
2. Test the value of variable (or condition, using while)
3. Alteration of variable value



i = 1
while i < 6:
    print(i)
    i+=1 #or i = i + 1, both are same

Q. Let n be a number given by the user, print its table till 10.
A. 
x = int(input("Enter the number: "))
i = 1
while i < 11:
    print(x*i)
    i+=1

Q. Given 2 integers x and n compute n power of all natural numbers till x.
A.
x = int(input("Enter the base value: "))
n = int(input("Enter the exponent value: "))
i = 1
while i <= x:
    print(i**n)
    i+=1

Q. Write a program to display sum of even numbers upto number n entered by the user.
A.

n = int(input("Enter the number: "))
i = 2
sum = 0
while i <= n:
    sum += i
    i += 2
print("The sum of even numbers till", n, "is", sum)

Python Class
08/07/2021

FOR LOOP:
RANGE FUNCTION: Start limit, stop limit, step limit

range(0,5,1)
Output → 0, 1, 2, 3, 4

If start value is not provided, default is 0, and step value is +1.

sum = 0
for i in range(2, 52, 2): #Here 'in' is the membership operator.
    sum+=i
print(sum) #Output → 650

sum = 0
for i in range(1, 51, 2):
    sum+=i
print(sum) #Output → 625


for i in range(51, 0, -2):
    print(i)

Q. Program to calculate even and odd integers of the first n natural numbers.
A. FOR ANS: 

n = int(input("Enter the number: "))
even=0
odd=0
for i in range(0, n+1, 2):
    even+=i
print("Even sum:", even)

for i in range(1, n+1, 2):
    odd+=i
print("Odd sum:", odd)

WHILE ANS:

n = int(input("Enter the number: "))
i = 2
sumeven = 0
while i <= n:
    sumeven += i
    i += 2
print("The sum of even numbers till", n, "is", sumeven)

j = 1
sumodd = 0
while j <= n:
    sumodd += j
    j += 2
print("The sum of odd numbers till", n, "is", sumodd)

Q. Find the factorial of n.
A. FOR ANS:
n = int(input("Enter the number whose factorial is to be found: "))
fac = 1
for i in range(1, n+1, 1):
    fac*=i
print("The factorial is", fac)

WHILE ANS:
n = int(input("Enter the number whose factorial is to be found: "))
fac1 = 1
i = 1
while i <= n:
    fac1*=i
    i+=1
print(fac1)

Q. Find the Fibonacci Series till n.
A.

n = int(input("Enter the number till where Fibonacci Series is to be found: "))
first = 0
second = 1
print(first)
print(second)
for x in range(0, n-2):
    nextnum = first + second
    first = second
    second = nextnum
    print(nextnum)

n = int(input("Enter the number till where Fibonacci Series is to be found: "))
f = 0
s = 1
i = 1
print(f)
print(s)
while i <= n-2:
    next = f + s
    f = s
    s = next
    i+=1
    print(next)

FOR LOOP is a COUNTING LOOP. WHILE LOOP is a CONDITIONAL LOOP.

Python Class
13/07/21


for i in range(0, 10):
    print(i)
    if i == 5:
        break
print("Out of loop.")

Aditya, [21.07.21 19:59]
[Forwarded from Gautam Prasanna Kappagal]
Q. Write a program to input some numbers repeatedly and find their sum. The program ends when the user says "No" or the program aborts when the number entered is less than 0.
A.
sum = 0
while True:
    n = int(input("Input: "))
    if n < 0:
        break
    sum += n
    ch = input("Do you want to enter more records? (Y/N): ")
    if ch == "N" or ch == "n":
        break
    elif ch == "Y" or ch == "y":
        continue
    else:
        print("Enter only Y or N.")
        ch = input("Do you want to enter more records? (Y/N): ")
print("The sum of the numbers you entered is", sum)

Python Class
14/07/21

s = "Python"
for i in s:
    if i == "t":
        break
    print(i)

Q1. Rewrite the following code fragment using for loop:
A1.
for i in range(100,0, -3):
    print(i)

Q3. Rewrite the following code fragment using while loop:
A3.
i = 1
while i < 10:
    if i%3 == 0:
        print(i)
    i+=1

Q4. WAP (Write A Program) to print the following series:
A4.
for i in range(1,41,3):
    print(i)

Q5. Identify the errors.
A5.
Num = 50
while Num >= 10:
    if Num == 30:
        break
    elif Num > 30:
        print(Num)
    else:
        print(Num//10)

PATTERN PRINTING PROGRAMS:

1 2 3
4 5 6
7 8 9

*

*
**


for i in range(1, 5):
    for j in range(1,i+1):
        print("*", end="")
    print()

for i in range(5,1,-1):
    for j in range(1,i):
        print("*", end="")
    print()

Q.
0
11
222
3333

A.
for i in range(1,5):
    for j in range(1,i+1):
        print(i-1, end="")
    print()

Q.
0
22
444
8888

A.
for i in range(1,5):
    for j in range(1,i+1):
        if i == 1:
            print(0, end="")
        else:
            print(2**(i-1), end="")
    print()

Python Class
20/07/21

x = "Python"
print(x[0])
#Here the 0 is an index value or subscript value, it goes from 0 to n.

print(x[3])

MUTABLE DATATYPES: Value of the string can be changed at the same memory location.
IMMUTABLE DATATYPES: Value of the string can not be changed at the same memory location.
STRING: Variables which take alphanumberic values.

x = "Python"
print(id(x))
x = "abcd"
print(id(x))

#STRING IS IMMUTABLE

y = 10
print(id(y))

y = "abc"
print(id(y))

x = " "
print(len(x))
print(x[0])

#SLICING
x = "Python"
print(x[::-1])
'''

'''22'/7/21 python class
x="python"
x[0]="y"
print(x)


#output error /// thus string is immutable
x="python"
for i in range (0,len(x)):
    #print(i)
    print(x[i])


#Capitalization
x="python is fun"
print(x.capitalize())


#count function
x="python is easy"
print(x.count('i'))

x="python is easy"
print(x.count('i',10,20))



#find function
x="python is fun"
print(x.find("z",9,12))


find - gives you -1 in case of no result
index- shows error


#index function
x= "python is easy"
print(x.index("z"))'''


'''#is digit function- checks for digit
x= "python is easy"
y="7"
print(x.isdigit())
print(y.isdigit())




#26/7/21

x="python"
print(x[-1])
print(x[-2])
print(x[4])

#This feature is called negative indexing.

x="python"
print(x.lower())
print(x.upper())
y= "Python123"
print(y.isalnum())

y= "123"
print(y.isalnum())

y= "%123"
print(y.isalnum())

y= "abc 123"
print(y.isalnum())


#isalnum = alphabet + number only


#Q) What will be the output of the following ?
str="i love india"
print(str[2:6])

#Q) FIND THE OUTPUT:
print("clas"+1+2+3)


#Q) 
print("abc DEF".split())
print("abc,DEF".split(","))

#SPLIT breaks one string into multiple strings at spaces and returns the strings in a list. 
# we can change the delimiter in the brackets using double quotes. 


x="python is fun"
y= x.split()
print(len(y))



#write a prog to calc the sum of digits present in a string.

x=(input("ENTER THE NO:ins "))
l=len((x))
y=0

for i in range(0, l):
    z=x[i]
    if z.isdigit()==True:
        y+=int(z)
print(y)

x=input(" enter no.: ")
#s=sum
s=0

for i in x:
    if i.isdigit()==True :
        s = s + int(i)

print(s)



'''

'''27/7/21


x="python is fun"
y=x.replace("fun","nice")
print(y)


#strip function: Eliminates leading or trailing spaces.
#lstrip,rstrip, strip

x="         Python is fun             "
print(x)
print(x.lstrip())
print(x.rstrip())
print(x.strip())


#titlecase- first letter of each word capitalize

x="python is fun"
y="Python is Fun"
print(x.istitle(), y.istitle())

z=(x.title())
print(z)



#starts with- checks for starting substring
# ends with- check for ending substring

x="python"
y="Python"

print(x.startswith("p"), y.startswith("p"))
print(x.endswith("n"), y.endswith("f"))



#q)write a program to count the number of lowercase letters in a string.

x=input("enter a word: ")
s=0

for i in x:
    if(i.islower()):
        s+=1

print("number of lowercase letters: ")
print(s)



#q)write a python program to check if a string is a palindrome or not.

x=input("enter word:")
if(x==x[::-1]):
    print("a  palindrome")

else:
    print("not a palindrome")



#q) Write a python program to change a character from a string.

x=input("enter a string: ")
y=input("enter string to be replaced: ")
z=input("enter string to replace with: ") 


a=(x.replace(y, z))



#q) write a program to check whether a substring is present in a given string or not. 

x=input("enter a string: ")
y=input("enter the substring to be checked: ")


if (x.find(y)==-1):
    print("substring is not present")

else:
    print(" present")



#q) write a program to count the word frequency in string.

x=input("enter string: ")
y=input("enter substring: ")

s=(x.count(y))

print(s)



#q)write a program to calculate the length of a string

x=input("enter a string: ")

y=0

for i in x:
    y+=1

print(y)


#q) write a python program to check if a string contains any special character or not .

X=input("enter a string: ")

y=(#,$,%,(,),[,])

if y=x:
    print("present")

else:
    print("not present")





# 28/7/21

#Swapcase- lowercase to uppercase, uppercase to lowercase

x="pythoN Is FUN"
print(x.swapcase())


#partition- divides string in 2 parts,  

x="Python is fun"
print(x.partition('i'))




x="Python is no fun"
print(x.partition(' '))
print(x.split('n'))


#max- max value(on ascii code)
#min- min (on ascii code)


#join- joins the string 
#iterable-list, (accessible 1by1 in loop), tuple, dictionary



x="Python is fun"
a={1, 2, 3}
y=':'
print(y.join(a))



#q)write a program to count the number of spaces in a given string.


x=input("enter a string: ")
s=0

for i in x:
    if(i.isspace()):
        s=s+1
print("The number of blank spaces is: ",s)


#q) write a program to count all occurances of o in a string.


s = "The quick brown fox jumps over the lazy dog."

print(s.count("o"))


#q) write a program to count the number of vowels in a string.

x=input("enter a string: ")

print("number of times a occurs: ", x.count('a'))
print("number of times e occurs: ", x.count('e'))
print("number of times i occurs: ", x.count('i'))
print("number of times o occurs: ", x.count('o'))
print("number of times u occurs: ", x.count('u'))

x = input()
y = ["a", "e", "i", "o", "u"]
n = 0
for z in x:
    if z.lower() in y:
        n+=1
print(n)


#q) write a program to take a string and replace every blank space with hyphen.

x=input("enter a string: ")
print(x.replace(' ','-'))


#q) write a program to get a string made of the first 2 and last 2 characters.


x=input("Enter a string:")
s=0
for i in x:
      s=s+1
new=x[0:2]+x[s-2:s]
print("new string :")
print(new)


#q) write a program to calc the no. of uppercase and lowercase letters.
x=input("enter string: ")
a=0
b=0
for i in x:
      if(i.islower()):
            a=a+1
      elif(i.isupper()):
            b=b+1
print("The number of lowercase characters is:")
print(a)
print("The number of uppercase characters is:")
print(b)


#q) write a program to calc no. of digits and letters in a string.

x = input()
d = 0
l = 0
for i in x:
    if i.isdigit() == True:
        d+=1
    elif i.isalpha() == True:
        l+=1
print("Digits: ", d)
print("Letters: ", l)

#WAP to get a string from a given string where all occurrences of its first char have been changed to '$' except the first char itself.









#q)write a program that inputs a string with multiple words, and then capitalize the first letter of each word.

x=input("enter string: ")

print(x.title())


29/7/21 


#q) write a program that reades a string and prints a string that capitalize alternate letters.


x=input("enter string: ")
  
print("The original string is : " + str(x))
  

# Alternate case in String
y = ""

for a in range (0,len(x)):
    z=x[i]
for i in range(len(x)):
    if not i % 2 :
       y = x[i].upper()
    else:
       y = x[i].lower()


print(y)






#q) write a python program to compute sum of digits in a given string.


#q)write a python program to get the last part of the string, after a specified char.

x=input("enter string: ")

y=input("charcter: ")

#q) write a python program to convert the given string to uppercase, if it contains atleast 2 uppercase char in the first 4 char

x=input("enter a string: ")

y=x(len(4))



#wap that does the following:
#1. takes 2 inputs: first an integer and second a string
#2. from input string extrct all digits in the order they occurred from the string
#3. add the integer input and digits extracted together as integers
#4. print the string in the form: integer input + digits = sum


i=int(input("enter a string: "))
s=str(input("enter a string: "))

l=0

for f in i:
    if f.isdigit()==True :
        l = l + int(f)

print(s)
'''

#5/8/21

#lists- it is a sequence datatype(String,etc) .

#1)- they hold multiple values ('3','4','5')
#2)-each element of the list can be accessed using an index.
#3)the concepts of -ve,+ve indexing and slicing exists.
#4) lists are not immutable. whereas strings are
#5)

'''' s=['Apple','banana','%',3, [ '1','3']]
s1=[]

s2=[1,2,3,4,5]

s2[0]=11
print(s2)

print(s2[-2])         #-ve indexing

x="python"
print(x[-1])
print(x[5])

y=list(x)
print(y)

#list is a built in function

s2=[1,2,3,4,5]

y=s2[0:4:2]
print(y)

#another list can be created from a list

x=eval(input("enter a list: "))
print(x)
print(type(x))

a=input("enter a list: ")
print(type(a))
#eval- works for multiple datatypes

10/8/21



x=[]
x=list()
print(type(x))

#list inside list is called nested list.
#list is a mutable datatype, elements can be changed at the same location


x=["1",1,["1","abc"]]
print(x[2])
print(x[0])
print(x[2][0])

x=["1",1,["1","abc"]]
x[1:3]=[1,2]
x[1:0]="1"

print(x)



x=["abc",123,"xyz"]
l=x
x[1]="pqr", "lmn"
print(l)

#shallowcopy- creating a copy of the list which is unaffected by the changes in the originals list.



x=["abc",1,2]
l=x.copy()
x[1]=11
print(l)
print(x)


#deepcopying-

import copy
x=["abc",1,["pqr","xyz"]]
l=copy.deepcopy(x)
x[1]=4
print(l)
print(x)

11/8/2021



#WAP to input two list and create a 3rd one that contains all the elemts of both the lists.

x=list(input("1st list: "))
y=list(input("2nd list: "))

z=x+y
print(z)



#WAP to put even and odd elements in a list, into 2 different list.
x=input("enter a list: ")

y=x.split
print(y)



#WAP to search for an element from a list of numbers.
x=list(input("enter a list: "))
y=int(input("enter a number:"))

d=0
for i in x:
    if i.isdigit():
        if int(i)==y:
            print(d)
        flag=1
        break

    d+=1

if flag==0:
    print("no number found")


x=[]
x.append("abcd")
x.append
x.extend
'''
'''APPEND: Adds the list as a single element and creates a nested list.
EXTEND: Adds the different elements of the list as individual elements in the list.'''

'''#12/8/21

#WAP that inputs a line of text and prints each word in a seperate line. Also print the count of words in the line.
#WAP to input a string and print each individual word of it along with its length.

x=input("enter a string: ")
#Write a program that removes all capitalization and common punctuation from a string s.
'''
#x = '''<>./?@#$%^&*_~!()-[]{};:'"\,'''

'''s = input("enter a string: ")
a = ""
for i in s:
   if i not in x:
       a+=i

print(a)

#WAP THAT READS email id of a person in the form of a string and ensures that it belong to domain @edupillar.com

x=str(input("enter the email id : "))
y="@edupillar.com"

if y in x:
    print("the email belongs to the domain")
else:
    print("the email address does not belong to the domain")


x = input()
if len(x) >= 15:
    if x[-1:-15:-1] == "moc.rellikude@":
        print("Correct Domain")
    else:
        print("Incorrect Domain")
else:
    print("Invalid email, enter characters before domain.")'''


#Q) Write a program that asks the users for a string and creates a new string that doubles each character of the originals string.

#(if the user inputs sito, output-ssiittoo



# 16/8/21

#WAP to write the second largest elements in a list num.
'''
num=[]
x=int(input("Enter number of elements:"))
for i in range(1,x+1):
    b=int(input("Enter element:"))
    num.append(b)
num.sort()
print("Second largest element is:",num[x-2])


num=list(input("enter a list: "))
s=num[0]

for i in range(1,len(num)):
    if num[i]>s:
        print(i)
        s=i
        s=num[i]
print(s)



#17/8/21
#INSERT-USED to insert an element in between the list.

l=[123,453,4647]
l.insert(0,465)
print(l)

l.insert(1,346)
print(l)

l.reverse()
print(l)

#INDEX- returns the index of the first occurence of the element in the list.

l=[1,2,3,3,4,5]
print(l.index(3))
print(l.index(7))    #ValueError:7 is not in the list


#SORT-

l=[1,2,3,4,5]

l.sort()
l.sort(reverse=True)
print(l)



#CLEAR-

l=[1,2,3,4,5]
l.clear()
print(l)


#COUNT-

l=[1,2,3,3,3,4,5]
print(l.count(3))

#DELETION- (del) (pop)- removes the argument at the index value. (remove)- argument is the element itself, not the index.

l=[1,2,3,4,5]
del l[0]
print(l)

l=[1,2,3,4,5]
l.pop(3) #IF no parameter provided, it deletes the last elements of the list.
print(l)

l=[1,2,3,4,5]
l.remove(4)
print(l)


#   Q) WAP to delete all odd numbers and -ve numbers in a numeric list.

x=eval(input("enter a list: "))

for i in x:
	if(i%2 != 0):
	    x.remove(i)

	if i<0:
		x.remove(i)
	i+=1

print(x)

#19/8/21


#Q) create a list , for i in l, printi, for i in range of length of l, print i.

l=list(input("enter a list: "))

for i in l:
    print(i)
for i   in range(len[l]):
    print(i)




#Q)# WAP in python inputing list from user and display those string which are starting from capital A

'''

#3/9/21

#Q) WAP to enter a list containing name of the week and the number, then create 2 different lists, one with string values and one with numerical values.
'''
x=['Monday',1,'Tuesday',2,'Wednesday',3,'Thursday',4,'Friday',5,'Saturday',6,'Sunday',7]

y=[]
z=[]

for i in range(len(x)):
    if i%2==0:
        y.append(x[i])

    else:
        z.append(x[i])
      

print(y)
print(z)

'''




#Tuples- ordered collection of objects

'''element can be of any datatype
tuple in tuple = nested tuple
()= declare tuple

Use tuples when needed for iteration, rather than editing'''

#WAP to create a tuple with numbers and print one item.
'''x=eval(input("enter tuple: "))

print(x[0])'''

#WAP to get the 4th element from the start, and 4th from the end of tuple.
'''
x=eval(input("enter tuple: "))

y=len(x)

print(x[y-4])
print(x[3])'''

#WAP to compare an element with every element within a tuple.
'''
x=eval(input("enter tuple: "))
y=eval(input("element to be compared : "))

for i in x:
    if y>i:
        print("element is greater. ")
    elif y<i:
        print("element is smaller. ")
    elif y==i:
        print("elements are equal. ")
    else:
        print("invalid input. ")'''


#WAp to convert list to a tuple.
'''
x=eval(input("ENTER LIST: "))
y=tuple(x)

print(x)
print(y)'''

'''
x=eval(input("enter tuple: "))
y=list(x)

print(x)
a=input("position of item to be removed: ")

x=tuple(y.remove(a))

print(x)'''

#Write a program to provide different list operations.
'''
x=[1,2,3,4,5,6,7,8,9,0]
print("list:",x)

print("A For Append, B for Insert, C for mOdify, D,E,F,G for Ascending sort, H for descending sort")

a=input("enter: ")

if a=='A':
    x.append()
    print(x)

elif a=='B':
    j=input("element to enter: ")
    x.insert(j)
    print(x)

elif a=='G':
    list.sort()
    print(x)

elif a=='H':
    list.sort(-1)
'''







#CS Practical File


#Practical1- Write  a program to show entered string is a palindrome or not.
'''x=input("enter word:")
if(x==x[::-1]):
    print("a palindrome")

else:
    print("not a palindrome")'''

#Practical2- Write a program to show statistics of characters in the given line(to counts the number of alphabets ,digits, uppercase, lowercase, spaces and other characters).
'''
x=input("input line : ")
a,b,c,d,e,f=0,0,0,0,0,0

for i in x:
    if(i.isspace()):
        a=a+1
    elif i.isdigit() == True:
        b=b+1
    elif i.isalpha() == True:
        c=c+1
    elif i.isupper() == True:
        d=d+1
    elif i.islower() == True:
        e=e+1
    else:
        f=f+1
print("The number of Blank Spaces is: ",a)
print("The number of Digits is: ", b)
print("The number of Alphabets is: ", c)
print("The number of Uppercase Letters is: ", d)
print("The number of Lowercase Letters is: ", e)
print("The number of Special Characters is: ", f)'''

#Practical3- Write a program to remove all odd numbers from the given list.

#Practical4- Write a program to display frequencies of all the element of a list.
'''# initializing the list
x= eval(input("enter list : "))
f = {}

for i in x:
   if i in f:
      f[i] += 1
   else:
      f[i] = 1

print(f)'''

#Practical5- Write a program to display those string which are starting with ‘A’ from the given list.

#Practical-
'''num = int(input("Enter the Number: "))
f = 1
i = 1
while i<=num:
    f = f*i
    i = i+1

print("Factorial =", f)'''

#Practical-
'''
x = input("enter values: ")
print(x)
print("Datatype of y = ", type(x))

y = tuple(x)

print(y)
print("Datatype of Fruits = ", type(x))
print("Datatype of y = ", type(y))'''

#Practical-
'''
num = eval(input("enter a list: "))
for i in range(len(num)-1):
    if num[i] % 7 == 0:
        num[i + 1], num[i] = num[i], num[i + 1]
print(num)'''

#Practical-
'''
list = eval(input("enter a list: "))

for i  in list:
    if(i%2 != 0):
        list.remove(i)

# print list after removing ODD elements
print("list after removing ODD numbers: ")
print(list)'''

#Practical-
'''
list = ['Eagle', 'Ants', 'Cats']

for word in list:
    if word[0]=='A':
        print(word)'''

#Practical-
'''
no=int(input("enter no of sections :"))

list={}

for i in range(no):
    a=input("enter section :")
    b=input("enter stream :")

    list[a]=[b]
    print("class","\t","section","\t","stream")

    for i in list:
        print("xi","\t",i,"\t","\t",list[i])'''

#Practical-
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1==num2:
    print("Both numbers are equal.")
else:
    print(max(num1, num2), "is greater")'''

#Practical-
'''
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)'''

#Practical-
'''
print("Enter 10 Elements of List: ")
list = []
for i in range(10):
    list.insert(i, input())
print("Enter an Element to Insert at End: ")
elem = input()
list.append(elem)
print("\nThe New List is: ")
print(list)'''

#Practical-
'''
str=input("to-read string: ")
new=""
for i in range (len(str)):
    if str[i].isupper():
        new+=str[i].lower()
    elif str[i].islower():
        new+=str[i].upper()
    else:
        new+=str[i]
print(new)'''

#Practical-
'''
l=eval(input("list: "))
item=eval(input("item to insert: "))
p=int(input("position: "))
l.insert(p-1,item)
print("updated list:",l)'''

#Practical-
'''
t=eval(input("Range(in form (a,b)(both inclusive): "))

print("non-prime nos: ")
for i in range(t[0],t[1]+1):
    p=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            p+=1
    if p!=0:
        print(i)
'''


#QUESTIONS
'''
#Q) What will be the output of the following expression(5<10)and(10<5)or(3>18)and not(8<18)

#Q)6*3+4**2/5-
#Q)WAP that takes a string wth multiple words and then capitalize the first letter of each word and forms a new string out of it.

x=input("enter multiple words with spaces in between: ")

y=x.split()
for i in y:
    z=i.capitalize()
    print(z)

'''



'''dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)'''

#25/11/21

#Q)Create dictionary to store 4 student details with rollno, name, age field. Search student in list.
''' s={'Klaus':{'Roll Number':'1', 'Age':'1001'},
    'Elijah':{'Roll Number':'2', 'Age':'1006'},
    'Rebekah':{'Roll Number':'3', 'Age':'1004'},
    'Freya':{'Roll Number':'4', 'Age':'1015'}

n = input("Enter name: ")
s1 = s[n]
print(s1)'''


#Q) write a python program to input names of n employs and their salary details like basic salary, house rent and convenience allowance. calculate total salary of each employ an display.
'''info=dict()
x= eval(input("no. of employees: "))

for i in range(x):
    a=input("name: ")
    b=int(input("basic salary: "))
    c=int(input("house rent: "))
    d=int(input("conveniance allowance: "))
    e=(b+c+d)

    info[a]=e

print(info)
'''

#Q2. WAP to input names of ‘n’ countries and their capital and currency, store it in a dictionary and display in tabular form. Also search and display for a particular country.
'''
info=dict()
x= eval(input("no. of countries: "))

for i in range(x):
    a=input("name: ")
    b=input("capital: ")
    c=input("currency: ")
    info[a]=b,c


print("country name","\t\t","|","\t\tcapital","\t\t","|","\t\tcurrency")
for j in range(x):
    print(i[j],"\t\t\t","|","\t\t",info[i[j]][0],"\t\t\t","|","\t\t",info[i[j]][1])
z=input("enter country to be searched: ")

print(info[z])
'''

#WAP to convert a no. entered into its corresponding number in words.
'''num= input("enter a number = ")
dic={"0":"zero","1":"one ","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}

for i in num:
      print(dic[i], end=" ")'''


#WAP  that repeatedly asks the user to enter product names and prices. Store all of them in a dictionary whose keys are product names and values are prices. Also write a code to search an item from the dictionary
'''
info=dict()

A = 'Y'
while True:
    n = input("name of product : ")
    p = input("Eprice of product : ")
    info[n] = p
    A = input("add more items (Y/N) : ")

z=input("enter product to be searched: ")
for i in info:
    if i==z:
        print("price of the product ",i," is ",info[i])
    else:
        print("not found")

'''

#Q. What will be the status of the following list after fourth pass of bubble sort arranging it in descending order?
#95, -1, 38, 2, 100, 65, 78


'''random.random()

#randrange(start,end,step)

print(random.randrange(2,6,2))

random.randint(4,1)'''

'''L=[1,2,3,4]
print(random.choice(L))
print(random.shuffle(L))
print(L)
'''

#q)GENERATE A RANDOM NUMBER BETWEEN
'''
def linearsearch():
    l=eval(input("enter list: "))
    x=input("no. to be searched: ")

    for i in range(0,l):
        if l[i]==x:
            print("element found")
            break
    else:
        ("element not found ")
linearsearch()
'''



#5/8/21

'''
#lists- it is a sequence datatype(String,etc) .

#1)- they hold multiple values ('3','4','5')
#2)-each element of the list can be accessed using an index.
#3)the concepts of -ve,+ve indexing and slicing exists.
#4) lists are not immutable. whereas strings are
#5)

s=['Apple','banana','%',3, [ '1','3']]
s1=[]

s2=[1,2,3,4,5]

s2[0]=11
print(s2)

print(s2[-2])         #-ve indexing

x="python"
print(x[-1])
print(x[5])

y=list(x)
print(y)

#list is a built in function

s2=[1,2,3,4,5]

y=s2[0:4:2]
print(y)

#another list can be created from a list

x=eval(input("enter a list: "))
print(x)
print(type(x))

a=input("enter a list: ")
print(type(a))
#eval- works for multiple datatypes
'''


#10/8/21

'''
x=[]
x=list()
print(type(x))

#list inside list is called nested list.
#list is a mutable datatype, elements can be changed at the same location


x=["1",1,["1","abc"]]
print(x[2])
print(x[0])
print(x[2][0])

x=["1",1,["1","abc"]]
x[1:3]=[1,2]
x[1:0]="1"

print(x)



x=["abc",123,"xyz"]
l=x
x[1]="pqr", "lmn"
print(l)

#shallowcopy- creating a copy of the list which is unaffected by the changes in the originals list.



x=["abc",1,2]
l=x.copy()
x[1]=11
print(l)
print(x)


#deepcopying-

import copy
x=["abc",1,["pqr","xyz"]]
l=copy.deepcopy(x)
x[1]=4
print(l)
print(x)
'''

#11/8/2021

'''
#WAP to input two list and create a 3rd one that contains all the elemts of both the lists.

x=list(input("1st list: "))
y=list(input("2nd list: "))

z=x+y
print(z)



#WAP to put even and odd elements in a list, into 2 different list.
x=input("enter a list: ")

y=x.split
print(y)



#WAP to search for an element from a list of numbers.
x=list(input("enter a list: "))
y=int(input("enter a number:"))

d=0
for i in x:
    if i.isdigit():
        if int(i)==y:
            print(d)
        flag=1
        break

    d+=1

if flag==0:
    print("no number found")


x=[]
x.append("abcd")
x.append
x.extend
'''
'''APPEND: Adds the list as a single element and creates a nested list.
EXTEND: Adds the different elements of the list as individual elements in the list.'''

#12/8/21
'''
#WAP that inputs a line of text and prints each word in a seperate line. Also print the count of words in the line.
#WAP to input a string and print each individual word of it along with its length.

x=input("enter a string: ")
#Write a program that removes all capitalization and common punctuation from a string s.
'''
#x = '''<>./?@#$%^&*_~!()-[]{};:'"\,'''

'''s = input("enter a string: ")
a = ""
for i in s:
   if i not in x:
       a+=i

print(a)

#WAP THAT READS email id of a person in the form of a string and ensures that it belong to domain @edupillar.com

x=str(input("enter the email id : "))
y="@edupillar.com"

if y in x:
    print("the email belongs to the domain")
else:
    print("the email address does not belong to the domain")


x = input()
if len(x) >= 15:
    if x[-1:-15:-1] == "moc.rellikude@":
        print("Correct Domain")
    else:
        print("Incorrect Domain")
else:
    print("Invalid email, enter characters before domain.")'''


#Q) Write a program that asks the users for a string and creates a new string that doubles each character of the originals string.

#(if the user inputs sito, output-ssiittoo


# 16/8/21
'''
#WAP to write the second largest elements in a list num.
num=[]
x=int(input("Enter number of elements:"))
for i in range(1,x+1):
    b=int(input("Enter element:"))
    num.append(b)
num.sort()
print("Second largest element is:",num[x-2])


num=list(input("enter a list: "))
s=num[0]

for i in range(1,len(num)):
    if num[i]>s:
        print(i)
        s=i
        s=num[i]
print(s)

'''

#17/8/21
'''
#INSERT-USED to insert an element in between the list.

l=[123,453,4647]
l.insert(0,465)
print(l)

l.insert(1,346)
print(l)

l.reverse()
print(l)

#INDEX- returns the index of the first occurence of the element in the list.

l=[1,2,3,3,4,5]
print(l.index(3))
print(l.index(7))    #ValueError:7 is not in the list


#SORT-

l=[1,2,3,4,5]

l.sort()
l.sort(reverse=True)
print(l)



#CLEAR-

l=[1,2,3,4,5]
l.clear()
print(l)


#COUNT-

l=[1,2,3,3,3,4,5]
print(l.count(3))

#DELETION- (del) (pop)- removes the argument at the index value. (remove)- argument is the element itself, not the index.

l=[1,2,3,4,5]
del l[0]
print(l)

l=[1,2,3,4,5]
l.pop(3) #IF no parameter provided, it deletes the last elements of the list.
print(l)

l=[1,2,3,4,5]
l.remove(4)
print(l)


#   Q) WAP to delete all odd numbers and -ve numbers in a numeric list.

x=eval(input("enter a list: "))

for i in x:
	if(i%2 != 0):
	    x.remove(i)

	if i<0:
		x.remove(i)
	i+=1

print(x)
'''


#Q)10/9/21
#Q) WAP t
'''
list=eval(input("enter a list: "))

for i  in list:
	if(i%2 != 0):
	    list.remove(i)

print("list after removing ODD numbers:")
print(list)


#Q) WAP which accepts a number from the user and prints the frequency of the number in the list.

#Q) WAP to display square of an elements if its an int, and change the case if an element is a str.

'''
'''
x=eval(input("enter a list: "))
y=0
z=0
for i in range(len(x)):
	if type(x[i])==int:
		x[i]=x[i]*x[i]
	elif type(x[i])==str:
		x[i]=x[i].swapcase()
print(x)
'''


'''
#WAP TO return the length of the shortest string in the tuple of strings.

#given tuple pairs, ((2,5),(4,2),(9,8),(12,10)) pair(a,b) count the no. of pairs such that both  a and b are even.

x=int(input("num1: "))
y=int(input("num2: "))

print("1 for addition, 2 for subtraction")
z=int(input("operation: "))

a=x+y
b=x-y
if z==1:
	print(a)
elif z==2:
	print(b)
else:
	print("invalid input.")
'''

#10/2/22
'''
#WAP to print the series:
#10 9 8.....1
# 1 -4 7 -10......-40

for i in range(10,0,-1):
    print(i)

n=int(input())
for i in range(0,n,1):
    print(n,((n+1)^3))



s= "This is a god"
print(s.upper())


x=int(input("first: "))
y=int(input("second: "))
z=int(input("third: "))
a=min(x,y,z)
b=max(x,y,z)
c=(x+y+z)-a-b
print("sorted: ",a,c,b)

print(chr(ord('b')+1))
"hello"+1+2+3
print(ord('b'-ord('a')))
'''


#Q1. Write a program with a user defined function to count the number of times a character (passed as argument) occurs in the given string.
'''
x=input("input string: ")
z=input("character to be searched: ")
def cnt():
    if z in x:
        a=x.count(z)
        print(a)
    else:
        print("not found")
cnt()
'''


#Q2. Write a program with a user defined function with string as a parameter which replaces all vowels in the string with '*'.
'''
x=input("enter string: ")

def re():
    vowels='aAeEiIoOuU'
    if vowels in x:
        x.replace(vowels,'*')
        print(x)
    else:
        print('wrong input')
re()
'''

#Q4. Write a program which reverses a string passed as parameter and stores the reversed string in a new string. Use a user defined function for reversing the string
'''
s=input("input string: ")
def replace():
    str =" "
    for i in s:
        str = i + str
    print(str)
replace()
'''

# Q3. Write a program to input a string from the user and print it in the reverse order without creating a new string.\
'''
s=input("input string: ")
s=s[::1]
print(str)
'''

#Q5. Write a program using a user defined function to check if a string is a palindrome or not. (A string is called palindrome if it reads same backwards as forward. For example, Kanak is a palindrome.)
'''
x=input("enter word:")
def check():
    if(x==x[::-1]):
        print("a  palindrome")
    else:
        print("not a palindrome")

check()
'''

#Q6. Write a user defined function to convert a string with more than one word into title case string where string is passed as parameter. (Title case means that the first letter of each word is capitalised)
'''
def convert():
    x = input("enter string: ")
    print(x.title())
convert()
'''

#Q7. Write a function deleteChar() which takes two parameters one is a string and other is a character. The function should create a new string after deleting all occurrences of the character from the string and return the new string.
'''
string=input("enter string: ")
char=input("enter char: ")
def deleteChar(string, char):
    str = ""
    for i in string:
        if i == char:
             continue
        else:
            str += i
    return str
'''

#QUESTIONS
'''
Q.1) Create a dictionary ‘ODD’ of odd numbers between 1 and 
10, where the key is the decimal number and the value is the 
corresponding number in words. Perform the following operations 
on this dictionary:
(a) Display the keys
(b) Display the values
(c) Display the items
(d) Find the length of the dictionary
(e) Check if 7 is present or not
(f) Check if 2 is present or not
(g) Retrieve the value corresponding to the key 9
(h) Delete the item from the dictionary corresponding to the key 9

Q.2) Q. Write a program to enter names of
employees and their salaries as input
and store them in a dictionary.

Q.3) Q. Consider the following dictionary stateCapital:
stateCapital = {"AndhraPradesh":"Hyderabad", 
"Bihar":"Patna","Maharashtra":"Mumbai", 
"Rajasthan":"Jaipur"}
Find the output of the following statements:
i. print(stateCapital.get("Bihar"))
ii. print(stateCapital.keys())
iii. print(stateCapital.values())
iv. print(stateCapital.items())
v. print(len(stateCapital))
vi print("Maharashtra" in stateCapital)
vii. print(stateCapital.get("Assam"))
viii. del stateCapital["Rajasthan"]
print(stateCapital)


Q.4) Q. TypeError occurs while statement 2 is running.
Give reason. How can it be corrected?
 >>> tuple1 = (5) #statement 1
 >>> len(tuple1) #statement 2

Q.5) Q. Write a program to read email IDs of n number of 
students and store them in a tuple. Create two new 
tuples, one to store only the usernames from the 
email IDs and second to store domain names from 
the email IDs. Print all three tuples at the end of the 
program. [Hint: You may use the function split()]

Q.6) Q. Write a program to input names of n students and 
store them in a tuple. Also, input a name from the 
user and find if this student is present in the tuple or not.







def per(a):
    z = 0
    for i in range(1, a):
        if a% i == 0:
            z = z+i
    return z == a
y=int(input("input: "))
print(per(y))


import math

def hcf(a,b):
    p=math.gcd(a,b)
    q=math.lcm(a,b)
    print("gcd: ",p)
    print("lcm: ",q)
hcf(10,20)




#Q3. Write a function to input a list, P, from the user and modify its content in such a way that the elements, which are multiples of 10 swap with the value present in the very next position in the list.

x=eval(input("enter list: "))

def modify():


'''

'''
pbook={}
x= int(input("no. of entries: "))

for i in range(x):
    a=input("name: ")
    b=int(input("phone number: "))
    pbook[a]=b
p= input("whose phone number to remove : ")

def findname():
    if p in pbook:
        del pbook[p]

findname()

print(pbook)
'''



'''a=int(input("start value: "))
b=int(input("stop value: "))
c=int(input("step value: "))

def count():
    for i in range(a,b,c):
        print(i)

count()



num=int(input("Enter a number:"))
last_digit=num%10
if(last_digit%3==0):
    print("{} is divisible by 3 ")
else:
    print("{} is not divisible by 3")
'''



'''n=int(input())
y=0
for i in range(n+1):
       if i%2==0:
           y=y+i
print(y)



n = int(input("Enter the number till where Fibonacci Series is to be found: "))
first = 0
second = 1
print(first,end=" ")
print(second,end=" ")
for x in range(0, n-2):
    nextnum = first + second
    first = second
    second = nextnum
    print(nextnum,end=" ")


#WAP to print the following pattern:
'''



# Write a program that checks for presence of a value inside a dictionary and prints its keys with ignore case.
'''d={1:'Apple',2:'Banana',3:'Orange'}
x=input("enter value: ")

if x in d.values():
    print("value exists in dictionary.")

else:
    print("error")

for k,v in d.items():
    if x==v:
        print(k)
'''

#Write a menu driven program to calculate: Area of circle [A=2] Area of square [A=a* a].Area of rectangle [A=1*b].
'''
print("1 for area of circle, 2 for area of square, 3 for area of rectangle: ")
x=int(input("enter your choice: "))

if x==1:
    r=int(input("enter radius of circle: "))
    print("Area of circle is: ",(3.14*r*r))

elif x==2:
    s=int(input("enter side of square: "))
    print("Area of square is: ",s*s)

elif x==3:
    l=int(input("enter length of rectangle: "))
    b=int(input("enter breadth of rectangle: "))
    print("Area of rectangle is: ",l*b)
else:
    print("wrong input")
'''

#Write a program to create a dictionary named year whose keys are month names and values are their corresponding number of days.
'''
year=dict()
n=int(input("no. of items: "))

for i in range(n):
    x=input("enter month name: ")
    y=input("enter no. of days in the month: ")
    year[x]=y
print(year)
'''

#Write a program that repeatedly asks the user to enter product names and prices. Store all of them in a dictionary whose keys are product names and values are prices. Also write a code to search an item from the dictionary.
'''
d=dict()
while True:
    x=input("enter product name: ")
    y=input("enter product price: ")
    d[x]=y
    print("do you want to add more items?(Y/N) ")
    j=input("enter: ")

    if j=='Y' or j=='y':
        continue
    else:
        break
a=input("item to search: ")

if a in d.keys():
    print("item is present.")
else:
    print("not present")
'''

#Write a program to create a tuple storing first 9 terms of Fibonnaci Series.
'''
l = [0,1]
a,b,c = 0,1,0

for i in range(7):
    c = a+b
    a = b
    b = c
    l.append(c)

print(tuple(l))
'''

#Write a function check(key) which takes a key as an argument and check whether that key is present in dictionary or not.
'''
d={"AndhraPradesh":"Hyderabad",
"Bihar":"Patna","Maharashtra":"Mumbai",
"Rajasthan":"Jaipur"}

def check(key):
    if key in d.keys():
        print("key is present.")
    else:
        print("key is not present.")

check("Bihar")
'''

#Write a program to Accept the number of terms say n from the user and display the dictionary in the form of {n: n*5}. For example: If number of terms entered by user is 4 then the expected dictionary is {1:5,2:10,3:15,4:20}.
'''
n=int(input("no. of terms: "))
d=dict()

for i in range(1,n+1):
    d[i]=i*5
print(d)
'''

#Write a program to display the maximum and minimum value in dictionary.
'''
d=dict()
x=int(input("no. of key value pairs needed ? : "))

for i in range(x):
    a=input("enter key: ")
    b=input("enter value: ")
    d[a]=b

for j in d.values():
    p=min(d.values())
    q=max(d.values())
    print("Minimum Value is ", p)
    print("Maximum Value is ", q)
    break
'''




#11/2/22




'''x=input("enter string: ")
l=x.split()
if "a" in l:
    print("present.")
    print(l.count("a"))
else:
    print("not present")

'''








#questions from cbse practicals--
'''  
 Input a welcome message and display it.
• Input two numbers and display the larger / smaller number.
• Input three numbers and display the largest / smallest number.

• Write a program to input the value of x and n and print the sum of the following series:
o 1+x+x2+x3+x4+.............xn
o 1-x+x2-x3+x4-.............xn
o x - x2 + x3 - x4 + .............xn
 2 3 4 n
o x + x2- x3+ x4- .............xn
 2! 3! 4! n!
 
 
 


'''


'''s=input("enter string: ")
L=s.split()
M=[]
for i in L:
    if len(i)==4:
        M.append(i)
    else:
        continue
n=len(M)
print("No of 4 letter words: ",n)
'''

'''
n=int(input("enter no. of integers: "))
l=[]
sodd=0
seven=0
for i in range(n):
for j in l:
    if j%2==0:
        seven+=j
    else:
        sodd+=j
print("sum of odd numbers: ",sodd)
print("sum of even numbers: ",seven)
'''



'''n=int(input("enter number: "))
s=0

for i in str(n):
    s+=int(i)**3
if s==n:
    print("y")
else:
    print("n")
'''


'''s=int(input("enter num: "))
n=str(s)
a=n[::-1]
print(n[::-1])
if a==n:
    print("a palindrome")
else:
    print("not")
'''


'''l=eval(input("enter list: "))
m=[]

for i in l:
    if i not in m:
        m.append(i)
print("final list: ",m)
'''



''''
l=eval(input("ENTER list: "))
m=[]
n=[]
for i in l:
    if i%2==0:
        m.append(i)
    else:
        n.append(i)
if len(n)>len(m):
    print("Unbalanced")
else:
    print("Balanced")
    
    
    
• Determine whether a number is a perfect number, an armstrong number or a palindrome.
• Input a number and check if the number is a prime or composite number.
• Display the terms of a Fibonacci series.
• Compute the greatest common divisor and least common multiple of two integers.
• Count and display the number of vowels, consonants, uppercase, lowercase characters in string.
• Input a string and determine whether it is a palindrome or not; convert the case of characters in a
string.
• Find the largest/smallest number in a list/tuple
• Input a list of numbers and swap elements at the even location with the elements at the odd
location.
• Input a list of elements, sort in ascending/descending order using Bubble/Insertion sort.
• Input a list/tuple of elements, search for a given element in the list/tuple.
• Input a list of numbers and find the smallest and largest number from the list.
• Create a dictionary with the roll number, name and marks of n students in a class and display the
names of students who have scored marks above 75.
'''


#• Determine whether a number is a perfect number, an armstrong number or a palindrome.
'''
n=int(input("enter number to check : "))
s=""
l=[]
l1=[]
sum=0
sum1=0
for i in range(1,n):       #for perfect number
    if n%i==0:
        l.append(i)
for i in l:
    sum+=i
if sum==n:
    print("N is a perfect number. ")

for i in str(n):
    sum1=sum1+(int(i)**3)
if sum1==n:
    print("N is a armstrong number.")

elif str(n)==(str(n)[::-1]):
    print("N is a palindrome.")
else:
    print("N is neither")
'''

#• Input a number and check if the number is a prime or composite number.
'''
n=int(input("enter number: "))
l=[]
for i in range(2,(n-1)):
    if n%i==0:
        l.append(i)

if len(l)==0:
    print("N is a prime number. ")
else:
    print("N is a composite number")
'''

#• Display the terms of a Fibonacci series.
'''
n=int(input("number of terms in fibonacci series: "))
a,b=0,1
print(a,end=" ")
print(b,end=" ")
for i in range(1,n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
'''

#• Compute the greatest common divisor and least common multiple of two integers.
'''
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter 1 for HCF, 2 for LCM, 3 for both."))

x=max(a,b)
l=[]
l1=[]
l2=[]
HCF=0
LCM=0
if c==1:
    for i in range(2,x-1):
        if x%i==0:
            l.append(i)
    l.sort(reverse=True)
    HCF=l[0:1]
    print("the hcf is: ",HCF)

if c==2:
    for i in range(1,a):
        if a%i==0:
            l1.append(i)
    for i in range(1,b):
        if b%i==0:
            l2.append(i)
    l=l1+l2
    print(l)
'''

#• Count and display the number of vowels, consonants, uppercase, lowercase characters in string.
'''
s=input("enter string: ")
def count(s):
    vowels=0
    consonants=0
    upper=0
    lower=0
    for i in s:
        if i.upper() in "AEIOU":
            vowels+=1
        if i.isupper()==True:
            upper+=1
        if i.islower()==True:
            lower+=1
        if i.upper() not in "AEIOU":
            consonants+=1
    print("No. of vowels: ",vowels)
    print("No. of consonants: ",consonants)
    print("No. of uppercase letters: ",upper)
    print("No. of lowercase letters: ",lower)
count(s)
'''

#• Input a string and determine whether it is a palindrome or not; convert the case of characters in a string.
'''
def palindrome(s):
    if s==s[::-1]:
        print("s is a palindrome")
    else:
        print("s is not a palindrome")
    
s=input("enter string to check for palindrome: ")
palindrome(s)
'''


#• Find the largest/smallest number in a list/tuple
'''
list=eval(input("enter list/tuple: "))
print("The largest number is: ", max(list))
print("The smallest number is : ", min(list))
'''

#• Input a list of numbers and swap elements at the even location with the elements at the odd location.
'''
list=eval(input("enter list of numbers: "))

for i in range(0,len(list),2):
    list[i+1],list[i]=list[i],list[i+1]
print(list)
'''

#• Input a list/tuple of elements, search for a given element in the list/tuple.
'''
l=eval(input("enter list of elements: "))
e=input("enter element to search: ")
count=0
for i in l:
    if e==i:
        count+=1

if count>=1:
    print("element is present.")
else:
    print("element is not present.")
'''

#• Create a dictionary with the roll number, name and marks of n students in a class and display the names of students who have scored marks above 75.

'''dict=dict()
n=int(input("number of students: "))
for i in range(n):
    name=input("enter name: ")
    marks=input("enter marks: ")
    dict[name]=marks

l=list()

for i in dict.values():
    if (dict[i])>75:
        print("The list of students having marks greater than 75: ", (dict[i]))




'''
#• Input a list of elements, sort in ascending/descending order using Bubble/Insertion sort.
'''
list=eval(input("enter list: "))
n=int(input("enter 1 for bubble sort, 1 for insertion sort: "))
if n==1:
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                    list[j],list[j+1]=list[j+1],list[j]
    print("List in ascending order: ",list)
    print("List in descending order: ",list[::-1])

#create program for insertion sort.


else:
    print("wrong input.")
'''


#Python Program for factorial of a number
'''
def factorial(n):
    product = 1
    for i in range(1,n+1):
        product=product*i
    print("The factorial of n is: ",product)
factorial(5)
'''

#Python Program for simple interest
'''
principal=int(input("enter principal amount: "))
rate_of_interest=int(input("rate of interest: "))
time=int(input("time: "))

def simpleinterest():
    simpleinterest=(principal*rate_of_interest*time)/100
    print(simpleinterest)
simpleinterest()
'''

#Python program to check whether a number is Prime or not
'''
n=int(input("number to check"))
l=[]
l1=[]
for i in range(2,n):
    l.append(i)
for j in l:
    if n%j==0:
        l1.append(j)
if len(l1)==0:
    print("n is prime")
else:
    print("n is non prime")
'''

#Python Program for n-th Fibonacci number
'''
firstnum=0
secondnum=1
l=list()
n=int(input("n: "))
sum=0
l.append(firstnum)
l.append(secondnum)

for i in range(1,n-1):
    sum = firstnum + secondnum
    firstnum=secondnum
    secondnum=sum

    l.append(sum)
print(l[-1])

'''

#Python Program for How to check if a given number is Fibonacci number?
'''
firstnum=0
secondnum=1
l=list()
n=int(input("number to check: "))
sum=0
l.append(firstnum)
l.append(secondnum)

for i in range(1,n):
    sum = firstnum + secondnum
    firstnum=secondnum
    secondnum=sum
    l.append(sum)
if n in l:
    print("fibonacci num")
else:
    print("nope")
'''

#Python Program for Sum of squares of first n natural numbers
'''
n=int(input("n: "))

def findsumofsquares(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i**2)
    print(sum)
findsumofsquares(n)
'''

#Write the code to convert the following string into List. “Sumitaarora”

'''
def strtolist(s):
    l=[]
    l.append(s)
    print(l)
strtolist("Sumitaarora")

'''
#Write a program to accept 10 numbers from the user and add even numbers in a list named “evenlist” and odd numbers in a list named “oddlist”.
'''
a=int(input("1:"))
b=int(input("2:"))
c=int(input("3:"))

print(max(a,b,c))
'''




# wap to display the no. of lines in a text file
'''
with open("filehandling.txt", "r") as f:
    d = f.readlines()
    print(len(d))
'''

#wap to display the size of a file after emoving leading and trailing white spaces
'''
with open("filehandling.txt", "r") as f:
    d = f.read()
    print(len(d.strip()))
'''

#wap to read a text file  and display the count of vowels and consonants in the file

'''
with open("filehandling.txt", "r") as f:
    d = f.read()
    consonants=0
    vowels=0
    for i in d:
        if i.isalpha():
            if i.lower() in ['a','e','i','o','u']:
                vowels+=1
            else:
                consonants+=1
    print("no. of vowels: ",vowels)
    print("no. of consonants: ",consonants)
'''

#wap to read a text fie line by line and display each word seperated by a hash

'''
with open("filehandling.txt", "r") as f:
    d = f.readlines()
    l=[]
    for i in d:
        j=i.split()
        for z in j:
            l.append(z)
    print(l)
    for i in l:
        print(i,end="#")
'''

#wap to display all the records in a file along with the line number:
'''
with open("filehandling.txt", "r") as f:
    d = f.readlines()
    l=[]
    c=0
    for i in d:
        c+=1
        print(c,":",i)
'''

#wa method in python to readlines from a text file to find and display the occurence of the word india.
'''
with open("filehandling.txt", "r") as f:
    d = f.read()

    a=d.count("india","INDIA","India")
    print(a)
'''





#practice 28/4/22

#Write a Python program to read an entire text file.
'''
with open("filehandling.txt", "r") as f:
    print(f.read())
'''

#Write a Python program to read first n lines of a file.
'''
with open("filehandling.txt", "r") as f:
    n=int(input("value of n: "))
    d=f.readlines()
    print(d[0:n])
'''

#Write a Python program to append text to a file and display the text.
'''
with open("filehandling.txt", "a") as f:
    f.write("noice bolte")
'''

#Write a Python program to read last n lines of a file
'''
with open("filehandling.txt", "r") as f:
    n=int(input("value of n: "))
    d=f.readlines()
    print(d[n:-1])
'''

#Write a Python program to read a file line by line and store it into a list.
'''
with open("filehandling.txt", "r") as f:
    d=f.readlines()
    print(d)
'''

#Write a Python program to read a file line by line store it into a variable.
'''
with open("filehandling.txt", "r") as f:
    d=f.readlines()
    s=""
    for i in d:
        s+=i
    print(s)
'''

#doubt
#Write a Python program to read a file line by line store it into an array.

#Write a python program to find the longest words.


##Write a python program to find the longest words.  #doubt
'''
with open("filehandling.txt", "r") as f:
    d=f.read()
    s=""
    print(d)
    l=d.split(" ")
    print(l)
    for i in l:
        if len(i)>len(i-1):
            l[i-1],l[i]=l[i],l[i-1]
    print(l)
'''

#Write a Python program to count the number of lines in a text file.
'''
with open("filehandling.txt", "r") as f:
    d=f.readlines()
    print(len(d))
'''

#Write a Python program to count the frequency of words in a file.
'''
with open("filehandling.txt", "r") as f:
    s=input("enter word of which frequency is to be count: ")
    d=f.read()
    print(d.count(s))
'''

#Write a Python program to get the file size of a plain file.
'''
with open("filehandling.txt", "r") as f:
    d=f.read()
    print(len(d))
'''

#Write a Python program to write a list to a file.
'''
with open("filehandling.txt", "a") as f:
    l=eval(input("list to write: "))
    for i in l:
        f.write(str(i))
'''



#29/3/22

#Write a menu driven python program and provide options to read, append,write a file.
'''
while True:
    i=int(input("enter 1 for reading, 2 for writing, 3 for appending, and 4 to exit the program: "))

    if i==1:
        f=open("filehandling.txt","r")
        print(f.read())
        f.close()
    elif i==2:
        f = open("filehandling.txt", "w")
        w=input("string to input: ")
        f.write(w)
        print("written successfully.")
        f.close()
    elif i==3:
        f = open("filehandling.txt", "a")
        w=input("string to input: ")
        f.write(w)
        print("appended successfully.")
        f.close()
    elif i==4:
        print("exited successfully.")
        break
    else:
        print("wrong input")
'''

'''
x=int(input("value of x: "))
n=int(input("value of n : "))
list=list()
sum=0
factorial=1
for i in range(1,n):
    i.append(list)

for j in range(1,n):
    for l in range(1, j+1, 1):
        factorial*=l
    sum=sum+(x**j/l)
print(sum)

'''




#BINARY FILE HANDLING MENU DRIVEN
'''
import pickle
lst = []

def read():
    try:
        file = open("filehandling.dat", "rb")
        data = pickle.load(file)
        print(data)
        file.close()
    except EOFError:
        print("no data in file !")
def write():
    file = open("filehandling.dat", "wb")
    x = int(input("1 to write more data, 2 to break: "))
    while True:
        if x == 1:
            roll_no = int(input("enter roll no : "))
            name = str(input("enter name : "))
            l = [roll_no, name]
            lst.append(l)
            print("written successfully")

        if x == 2:
            pickle.dump(lst, file)
            break

        x = int(input("1 to write more data, 2 to break: "))
    file.close()
def append():
    with open("filehandling.dat", "rb+") as file:
        data = pickle.load(file)
        roll_no = int(input("enter roll no: "))
        name = input("enter name: ")
        l1 = [roll_no, name]
        data.append(l1)
        # data.append([roll_no,name])
        file.seek(0)
        pickle.dump(data, file)

    # return data
def search():
    file = open("filehandling.dat", "rb")
    data = pickle.load(file)
    s = int(input("Roll no to search: "))
    for i in data:
        if i[0] == s:
            print("Element found:  ", i[1])
def update():
    file = open("filehandling.dat", "rb+")
    data = pickle.load(file)
    roll_no = int(input("Roll no to update: "))
    name = input("Name to change to: ")
    for i in data:
        if i[0] == roll_no:
            i[1] = name
            print(data)
    file.seek(0)
    pickle.dump(data, file)
    print("Updated Sucessfully.")
def delete():
    file = open("filehandling.dat", "rb+")
    data = pickle.load(file)
    roll_no = int(input("Enter roll no to delete : "))
    for i in data:
        if i[0] == roll_no:
            j = data.index(i)
            data.remove(data[j])
    file.seek(0)
    pickle.dump(data, file)
    print("Data after deletion: ", data)
    print("Record deleted successfully.")
def format():
    f = open("filehandling.dat", "wb")
    d = ""
    pickle.dump(d, f)
    print("Format successful.")

print("---Menu---\n Reading(Press 1)\n Writing(Press 2)\n Appending(Press 3)\n Search(Press 4)\n Update(Press 5)\n Exiting(Press 6)\n Formatting the file(Press 7)\n Delete a record(Press 8)\n")
a = int(input(" Your Choice: "))
while True:
    if a == 1:
        read()
    if a == 2:
        write()
    if a == 3:
        append()
    if a == 4:
        search()
    if a == 5:
        update()
    if a == 6:
        print("exited successfully")
        break
    if a == 7:
        format()
    if a == 8:
        delete()

    print("---Menu---\n Reading(Press 1)\n Writing(Press 2)\n Appending(Press 3)\n Search(Press 4)\n Update(Press 5)\n Exiting(Press 6)\n Formatting the file(Press 7)\n Delete a record(Press 8)\n")
    a = int(input(" Your Choice: "))

'''



#26/5/22


#waf to search and display details whose destination is cochin from bus.dat.
#list data- bus startingpoint,busnom,bus details
'''
def writeinbus():
    file = open("filehandling.dat", "wb")
    x = int(input("1 to write more data, 2 to break: "))
    lst=[]
    while True:
        if x==1:
            startpoint = input("enter starting point : ")
            destination = input("enter destination : ")
            bus_no=int(input(" bus no: "))
            l = [startpoint,destination,bus_no]
            lst.append(l)
            print("written successfully")
        elif x==2:
            break

        x=int(input("1 to write more data, 2 to break: "))
    pickle.dump(lst, file)
    file.close()

writeinbus()
file=open(filehandling.dat","rb")
data=pickle.load(file)

for i in data:
    if i[1].lower()=="cochin":               #nested list [starting point,ending point,bus num, ..."
        print(i)
'''



#wap to count the number of records stored in a binary file marks.dat
'''
def writeinmarks():
    file = open("marks.dat", "wb")
    x = int(input("1 to write more data, 2 to break: "))
    lst=[]
    while True:
        if x==1:
            roll_no = int(input("enter roll no : "))
            name = input("enter name : ")
            marks= int(input(" enter marks: "))
            lst.append([roll_no, name,marks])
            print("written successfully")

        if x==2:
            pickle.dump(lst, file)
            break

        x=int(input("1 to write more data, 2 to break: "))
    file.close()

writeinmarks()
file = open("marks.dat", "rb")
data=pickle.load(file)
counter=0

for i in data:
    counter+=1
print("no of records: ",counter)
'''


# waf add records to add more records at the bottom of the file employ.dat
#list data- [employ_no,employ_name,employ_desgination]
'''
f=open("filehandling.dat.dat","wb")
f.close()

def append():
    with open("filehandling.dat","rb+") as file:
        x=int(input("Press 1 to Enter More Data\nPress 2 to Break\nYour Choice : "))
        try:
            data=pickle.load(file)
            while True:
                if x==1:
                    employ_no=int(input("Enter Employee No : "))
                    employ_name=input("Enter Employee Name : ")
                    employ_designation=input("Enter Employee Designation : ")
                    data.append([employ_no, employ_name,employ_designation])
                if x==2:
                    file.seek(0)
                    pickle.dump(data, file)
                    print("\nData Added Successfully !")
                    break
                x=int(input("Press 1 to Enter More Data\nPress 2 to Break\nYour Choice : "))
        except Exception:
            print("Please Check before Entering !")
append()
'''


##waf search()to display the record of a particular product from a afile product.dat whose code is passed as an argument
#[product_code,porduct_price]
'''
def write():
    file=open("filehandling.dat","wb")
    data=[]
    a = int(input("Press 1 to Enter More Data\nPress 2 to Save\nYour Choice: "))
    while True:
        if a==1:
            product_code=int(input("Enter Product Code : "))
            product_name=input("Enter Product Name: ")
            product_price=int(input("Enter Product Price: "))
            data.append([product_code,product_name,product_price])
            a = int(input("Press 1 to Enter More Data\nPress 2 to Save\nYour Choice: "))
        else:
            break
    pickle.dump(data,file)
    print("Data Written Successfully !")

def search():
    file = open("filehandling.dat", "rb")
    data=pickle.load(file)
    a=1
    while a==1:
        product_code=int(input("Enter Product Code : "))
        for i in data:
            if i[0]==product_code:
                print("Product Found\n\n Product Details: ",i)
        a=int(input("Press 1 to search more records\nPress 2 to Exit\n\nYour Choice: "))

x=int(input("Press 1 to Write Data in the File\nPress 2 to Search Data in the File\nPress 3 to Exit the Menu\n\nYour Choice: "))
while True:
    try:
        if x==1:
            write()
        if x==2:
            search()
        if x==3:
            break
        elif x!=1 and x!=2 and x!=3:
            print("Please Enter Correct Option.")
        x = int(input("Press 1 to Write Data in the File\nPress 2 to Search Data in the File\nPress 3 to Exit the Menu\n\nYour Choice: "))
    except Exception:
        print("An Error Occured.\n")

'''










##CSV(comma sepereated Values) FILE HANDLING MENU DRIVEN
'''
def read():
    file = open("filehandling.csv", "r")
    try:
        cr = csv.reader(file)
        print("\nPrinting Data......\n")
        for i in cr:
            print(i)
        print("\n")
    except Exception as e:
        print("An Error occured....... Error: ",e)
    file.close()
def write():
    file=open("filehandling.csv","w",newline="")
    cw=csv.writer(file)
    list=[["roll no","name"]]
    roll_no = int(input("enter roll no: "))
    name = input("enter name: ")
    #print("\nWriting........")
    print("Written Successfully\n")
    list.append([roll_no, name])

    x=int(input("Press 1 to Enter More Records\nPress 2 to Exit\n\nYour Choice:"))
    while True:
        if x==1:
            roll_no=int(input("enter roll no: "))
            name=input("enter name: ")
            list.append([roll_no,name])
            print("\nRecords Added Successfully.\n")
        if x==2:
            cw.writerows(list)
            print("Exited successfully.")
            break
        x = int(input("Press 1 to Enter More Records\nPress 2 to Exit\n\nYour Choice:"))
    file.close()
def append():
    file = open("filehandling.csv", "a", newline="")
    list = [["roll no", "name"]]
    roll_no = int(input("enter roll no: "))
    name = input("enter name: ")
    cw=csv.writer(file)
    data=[roll_no,name]
    cw.writerow(data)
    file.close()
def search():
    file = open("filehandling.csv", "r")
    cr=csv.reader(file)
    roll_no=input("enter roll no to search: ")
    #print("Searching..")
    for i in cr:
        #print("..")
        if i[0]==roll_no:
            print("Data Found.")
            print(i)
def update():
    data=[]
    file = open("filehandling.csv", "r")
    cr=csv.reader(file)
    #print("Updating...")
    for i in cr:
        #print("...")
        data.append(i)
    file.close()
    roll_no=input("\nRoll no to update: ")
    name=input("Name to change to: ")
    for i in data:
        if i[0]==roll_no:
            i[1]=name

    file = open("filehandling.csv", "w",newline='')
    cw=csv.writer(file)
    cw.writerows(data)
    print("\nData Updated Successfully.")
    file.close()
def delete():
    data = []
    file = open("filehandling.csv", "r")
    cr = csv.reader(file)
    #print("\nDeleting......")
    for i in cr:
        #print("...")
        data.append(i)
    file.close()
    roll_no = str(input("\nRoll no to delete: "))
    for i in data:
        #print("...")
        if i[0]== roll_no:
            index=data.index(i)
            data.remove(data[index])

    file = open("filehandling.csv", "w",newline='')
    cw = csv.writer(file)
    cw.writerows(data)
    file.close()

    print("\nData Deleted Successfully.")

a=int(input("---Menu---\n\nPress the number corresponding to the functions written below to execute them.\n\nReading(1)\nWriting(2)\nAppending(3)\nSearching(4)\nUpdating(5)\nDeleting(6)\nPress 7 to Exit\n\nYour Choice: "))
while True:
    if a==1:
        read()
    if a==2:
        write()
    if a==3:
        append()
    if a==4:
        search()
    if a==5:
        update()
    if a==6:
        delete()
    #if a!=1 or a!=2 or a!=3 or a!=4 or a!=5 or a!=6:
        #exit()
    if a==7:
        exit()
    a = int(input("---Menu---\n\nPress the number corresponding to the functions written below to execute them.\n\nReading(1)\nWriting(2)\nAppending(3)\nSearching(4)\nUpdating(5)\nDeleting(6)\nPress 7 to Exit\n\n Your Choice: "))
'''
