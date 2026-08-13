
'''
#1
a=int(input("Enter first  number:"))
b=int(input("Enter secound number:"))
c=int(input("Enter third number:"))
if a >=b and a >=c:
      print("Largest =",a)
elif b >=a and b >=c:
      print("Largest =",b)
else:
      print("Largest =",c)
#2
a=int(input("Enter first  number:"))
b=int(input("Enter secound number:"))
c=int(input("Enter third number:"))
if a <=b and a <=c:
      print("Largest =",a)
elif b <=a and b <=c:
      print("Largest =",b)
else:
      print("Largest =",c)
#3
n=int(input("Enter a number:"))
if n>0:
      print("positive")
elif n<0:
      print("negative")
else:
      print("zero")
#4
k=int(input("Enter number of late days:"))
if k <=5:
      fine =d*0.40
elif k <=10:
      fine =d*0.65
else:
      fine =d*0.80
print("fine =",fine)
#5
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter operator(+,-,*,/):"))
if op =="+":
      print("answer =",a+b)
elif op =="-":
      print("answer =",a-b)
elif op =="*":
      print("answer =",a*b)
elif op =="/":
      print("answer =",a/b)
 else:
       print("Invalid operator")
 
 #6
 n=int(input("enter a number:"))
 if n%5==0 and n%3==0 and n%7==0:
       print("multiple of 5,3 and 7")
 else:
       print("Not a multiple of 5,3 and 7")
 #7
 w=int(input("Enter weight in gm:"))
 t=input("Enter booking type(O/E):")
 if t == "0":
     if w <=100:
         charge =80
     elif w <=500:
         charge =150
     elif w <=1000:
         charge =210
     else:
         charge =250
 elif t =="E":
       if w<=100:
         charge =100
       elif w <=500:
         charge =200
       elif w <=1000:
         charge =250
 else:
       print("Invalid booking type")
       charge=0
       print("charge =",charge)
 
 #8
 price= int(input("Enter laptop price:"))
 if price <=5000:
       dis =0
 elif price <=100000:
       dis =price *10/100
0 commit comments
Comments
0
 (0)
Comment
You're not receiving notifications from this thread.

 
