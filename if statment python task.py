Skip to content
karthickrajak155-web
karthick.python
Repository navigation
Code
Issues
Pull requests
Agents
Actions
Projects
Security and quality
Insights
Commit 16ce7b1
karthickrajak155-web
karthickrajak155-web
authored
last month
Verified
Add files via upload
main
1 parent 
059e5e7
 commit 
16ce7b1
1 file changed

+157
Lines changed: 157 additions & 0 deletions
File tree
Filter files…
if python.py
Search within code
 
‎if python.py‎
+157
Lines changed: 157 additions & 0 deletions
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,157 @@
'''
#(1)(2)find the smallest and largest number
number="2"
if number>="5":
        print("the number is smalest number ")
else:
    print ("the number is largest number  ")
#(3)absalute value
password="correct"
if password=="correct":
    print("allowed to access the lab")
#(4)odd or even
a=int(input("enter the munber :"))
if a%2==0:
    print("even numver")
else:
    print("odd number")
#(5)(6)multiple by 5 and 10
a=int(input("enter the number :"))
if a%5==0 and a%10==0:print("the given number is multiple by 5 and 10")
else:
    print("not a multiple of 5 and 10")
#(7)two-digit  number or not
number=int(input("enter the number :"))
value3=int(input("enter the value:"))
if number>=10 and number<=99:
    print("the number is a 2 digit")
    if value3>=100 and value3<=:
        print("the value is 3 digit ")
    else:
        print("the value is not a 3 digit")
else:
    print("the number is not a 2 digit")
    
# 8 three digit  number                 
num=int(input("enter the number :"))
if num/100>=1 and num/100<10:
    print("the number is 3 dig number")
else:
    ptrint("the number is not 3 dig number")
    
#9
a=["10","20","30","40","50","60","70","80","90","100"]
b=input("enter the value:")
if a==b: 
 print("the number ends with 0")
else:
 print("the munber not ends with 0")
#10
number=int(input("enter the number :"))
aim=number**2
if number>50:
    print("the squre root is above 50")
else:
    print("the squre root is bellow 50")
#11
value1=int(input("enter a number:"))
value2=int(input("enter another number:"))
difference=value1-value2
if difference==0:
    print("the difference is 0")
else:
    print("the difference is not a 0")
#12
print("computer science marksheet")
mark=int(input("enter your marl:"))
if mark>=50:
    print("pass")
else:
    print("fail")
#13  
number=int(input("enter a number :"))
if number%10==0:
    print("accept")
else:
     print("not")
#14
number=int(input("enter a number :"))
if number<=10 and number>=99:
    print("the number is 2 digit")
else:
    print("the number is not 2 digit")
#15
value=int(input("enter your choice:1"))
if value==1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")
#16
value=int(input("enter a value:"))
if value==1:
        print("you can go out and play")
else:
    print("you cannot go and play")
#17
lenth=int(input("enter a lenth:"))
breth=int(input("enter a breth:"))
if lenth==breth:
    print("same")
else:
    print("not same")
#18
value=int(input("enterb a value"))
if value>=65 and value<=90:
    print("it is an ASII uppercase")
else:
     print("it is not an ASII uppercase")
#19
value=int(input("enterb a value"))
if value>=97 and value<=119 :
    print("it is an ASII lowercase")
else:
     print("it is not an ASII lowercase")
#20
num = int(input("Enter an ASCII value: "))
if num >= 48 and num <= 57:
    print("It is the ASCII value of a numeric character")
else:
    print("It is not the ASCII value of a numeric character")
    
#22
number=int(input("enter a number:"))
if number5 and number=*3:
    print("it is multiple by 3&5")
else:
    print("it is ot multiplr of 3&5")
#23
number=int(input("enter a number:"))
if number<=100 and number>=999 and number%2==0 and number%5==0 and number*10==0:
    print("it is a multiple of 2,5,10")
else:
    print("it is not a multiple of 2,5,10")
#24
value1=int (input("enter value 1:"))
value2=int (input("enter value 2:"))
if value1%2==0 and value2%2==0:
    print("product",value1*value2)
else:
    print("sum",value1+value2)
0 commit comments
Comments
0
 (0)
Comment
You're not receiving notifications from this thread.

 
