'''
#1
n = int (input("enter n: "))

for i in range (1,n+1):
    print(i,end=" ")
#2
n= int (input("enter n: "))

for i in range (1,n+1):
    print(2 * i,end=" ")
#3
n = int (input("enter n :"))

for i in range (1,n+1):
    print(2*i-1,end=" ")
#4
n = int(input("enter n:"))

for i in range (1,n+1):
    print(3*i,end=" ")
#5
n= int(input("enter n:"))

for i in range (1,n+1):
    print(5*i,end=" ")
#6
n= int(input("enter n:"))

for i in range (2,n+1 ,2):
    print(i,end=" ")

#7
n = int(input("enter n:"))

for i in range (1,n+1):
    if i%2 ==0 or i%3 == 0:
        print(i,end=" ")

#8
n = int (input("enter n:"))
for i in range (1,n+1):
    if i%2 ==0 or i%5 ==0:
               print(i,end=" ")

12#9
n = int(input("enter n:"))
for i in range(1,n+1):
    if i%3 ==0 or i%5 ==0 or i%7 ==0:
        print(i,end=" ")

              
#10
n = int(input())
digit=0
sum = 0
while n > 0:
    digit =n % 10
    sum = sum + digit
    n = n// 10
print(sum)
    
#11
n = int(input())
count = 0
while n > 0:
    n = n// 10
    count+=1
print(count) 
#12
n = int(input())
for i in range (1,n+1):
    if n%i==0:
        print(i)
#13
n = int(input())
c=0
for i in range (1,n+1):
    if n%i==0:
        c+=1
print(c)
#14
n = int(input())
count = 0
for i in range(1,n+1):
    if n% i ==0:
        count = count + 1
if count ==2:
    print("prime")
else:
    print("not prime")
    
#15
n = int(input("enter the number:"))

for i in range(2, n +1):
    prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j ==0:
            prime = False
            break
    if prime:
            print(i,end=" ")

#16
n = int(input("enter the value:"))
m= int(input("enter the bvalue:"))
c=0
for i in range (1,n+1):
    if m%i ==0 and n%i==0:
      c=i
print(c)

#17
n  = int(input("enter the value:"))
m = int(input("enter the value:"))
for i in range(1,n+1):
    if m%i ==0 and n%i==0:
        print(i)
        
#18
a=0
b=1
for i in range (20):
    if a< 50:
        break
    print(a, end=" ")
    c = a+b
    a = b
    b = c

n = int(input("enter the value:"))
fact = 1
for i in range (1,n+1):
    fact = fact * 1
    print("factorial=",fact)

#20
odd = 0
even = 0
for i in range (n):
    num = int(input("enter the integer:"))
    if num % 2 == 0:
        even_sum += num
        odd_sum += num
    else:
        odd_sum +=num
        print("even sum of number:",even_sum)
        print("odd sum of number:",odd_sum)

n =  153
n1 = n
n2 = n
c =0
while n>0:
    n = n//10
    c+=1

s=0
while n1>0:
    r = n1 % 10
    s = s +(r**c)
    n1 = n1//10
if n2 ==5:
    print("armstrong number")
else:
    print("not a armstrong number")

'''


































