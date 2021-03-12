'''
import module1
from module2 import *
from module3 import m3_first
a=module1.add(1,2,3,4)
print(a)
l=["purva","kira","bhagu","triple"]
print(module1.rev(l))
m3_first()
print(module1.life)
module1.life="kira"
print(module1.life)
'''
'''
#import module1
import vita.my_pack.module1 as m
a=m.add(1,2,3,4)
print(a)
l=["purva","kira","bhagu","triple"]
print(m.rev(l))
print(m.life)
m.life="kira"
print(m.life)
'''
'''
d={"a":"purva","b":"kira","c":"bhagu","a":"lm"}
for i,j in d.items():
    print(i,j)
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
'''
'''
my_list = [4, 7, 0, 3]

a=iter(my_list)#make object iterable
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))#Err stopiteration
'''
# create an iterator object from that iterable
#l=[1,2,3,4]
#iter_obj = iter(l)
'''
# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        print(element)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
    finally:
        pass

'''
#init self
'''
def pk():
    print(1)
    print(2)
    print(3)
    yield
    print(4)
    print(5)
    print(6)
    print(7)
    yield
    print(8)
    print(9)
    yield
    
a=pk()
next(a)
next(a)
#next(a)
'''
#iterator
#protocol  iter and next
#implicitly call __iter__() and __next__() method
'''
   1
  121
 12321
1234321
'''
'''
count=3
for i in range(2,6):
    print(" "*count,end='')
    for j in range(1,i):
        print(j,end='')
    if count<3:
        for k in range(i-2,0,-1):
            print(k,end='')
    count=count-1
    print("\n")
'''
'''
class A():
    "this is A class"#this always hould be on first line
    name="kira"
    cls_attr=100
    def __init__(me,num):
        me.num=num
    def start(me):
        print("started")
    def set_attr(me,num):
        me.num=num
    def get_attr(me):
        return me.num
        
a=A(200)
#a.set_attr(10)
A.start(a)
print(A.name)
'''
'''
class parent1():
    "this is parent class"
    name="parent"
    age=20
    def __init__(self):
        print("in parent1 constr")
    def p1(self):
        print("parent1 p1")
    def p2(self):
        print("parent1 p2")
class parent2():
    "this is parent class"
    name="parent"
    age=20
    def __init__(self):
        print("in parent2 constr")
    def p1(self):
        print("parent2 p1")
    def p2(self):
        print("parent2 p2")



class child(parent1,parent2):
    "this is child class"
    name="child"
    def __init__(self):
        print("in child constr")
    def c1(self):
        print("child c1")
    def c2(self):
        print("child c2")
    
c=child()
print(child.__mro__)
'''
'''
class A():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "class A"
    def __add__(a,b):
        return a.a+a.b+b.a+b.b
    
a=A(1,2)
b=A(3,4)
print(a+b)
'''
'''
#iterator
class A():
    def __init__(self):
        print("instantiated class A")
        
    def __iter__(self):
        self.start=0
        self.end=5
        self.step=1
        self.sum=0
        return self
    def __next__(self):
        result=0
        if self.start<(self.end):
            self.start=self.start+self.step
            return self.start*2
        else:
            return "no element left"
a=A()
i=iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
'''
'''
def pk():
    print(1)
    print(2)
    print(3)
    yield
    print(4)
    print(5)
    print(6)
    print(7)
    yield
    print(8)
    print(9)
    yield
    
a=pk()
next(a)
next(a)
'''
'''
def a(k):
    for i in k:
        yield i
        
for i in a("kira"):
    print(i)
'''
#decorator

'''
# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    #print(a, b, c, d)
     return a+b+c+d
# Driver Code

my_list = [1, 2, 3, 4]
 
# Unpacking list into four arguments
a=fun(*my_list)
print(a)

def fun(*a):
    #print(a, b, c, d)
     pass
# Driver Code

my_list = [1, 2, 3, 4]
 
# Unpacking list into four arguments
a=fun(1, 2, 3, 4)

'''
'''
n=int(input("enter number"))
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

print(fact(n))
'''
'''
n=int(input("enter number"))
def bin(n):
    if n==0:
        return
    bin(n//2)
    print(n%2,end='')
    
bin(n)
'''
'''
t1=0
t2=1
for i in range(0,5):
    print(t1)
    tn=t1+t2
    t1=t2
    t2=tn
'''
# Python program to display the Fibonacci sequence

'''
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
    
for i in range(5):
    print(recur_fibo(i))
'''
#hcf
'''
n,m=int(input()),int(input())
a=min(n,m)

for i in range(n,0,-1):
    if n%i==0 and m%i==0:
        print(i)
        break
'''      
'''
def hcf(n,m,i):
    if n%i==0 and m%i==0:
        print(i)
        return
    else:
        hcf(n,m,n-1)
'''
'''
n,m=int(input()),int(input())
for i in range(max(n,m),n*m+1,m):
    if i%m==0 and i%n==0:
        print(i)
        break
'''
'''
n,m=int(input()),int(input())
def lcm(n,m,i):
    if i%m==0 and i%n==0:
        print(i)
        return
    else:
        lcm(n,m,i+m)
lcm(n,m,m)
'''
#string
#print(input("enter string").count(input("enter string")))

#s=input("enter string : ")
#print("palindrome" if s==s[::-1] else "not palindrome")


#print(input("enter string").count(input("enter word")))
'''
s=str.split(input("enter string"))
for i in s:
    print(i[::-1])

'''
'''
s1="one three five"
s2="two three four"
for i in zip(s1.split(),s2.split()):
    print(''.join(i))
'''
#print("same" if input("enter first string")==input("enter second string") else "not same")

'''
s="stanmit"
c='t'
k=s.replace(c,'')
print(k)
'''
#s=[1,2,1,3,1]
#print(9 in s)
'''
l=[5,1,36,47,2]
for i in range(len(l),1,-1):
    for j in range(0,i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
'''
'''
l1=[[1,2],[3,4]]
l2=[[1,2],[3,4]]
l3=[[0,0],[0,0]]
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
       l3[i][j]=l1[i][j]+l2[i][j] 

print(l3)
'''
'''
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[1,2,3],[4,5,6],[7,8,9]]
l3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            l3[i][j]=l1[i][k]*l2[k][j]
print(l3)
'''
'''
l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
k=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print(l)
for i in range(len(l)):
    for j in range(len(l[0])):
        k[i][j]=l[j][i]
print(k)
'''
'''
l=[45,66,154,15,665]
for i in range(len(l)):
    min=i
    for j in range(i,len(l)):
        if l[min]<l[j]:
            min=j
    l[i],l[min]=l[min],l[i]
    
print(l)
'''     
'''
l=[1,5,78,9,6,4,7,2,1,6]
l.sort()
element=78
start=0
end=len(l)-1
mid=0
while start<=end:
    mid=(start+end)//2
    if element==l[mid]:
        print("yes")
        break
    if element < l[mid]:
        end=mid-1
    else:
        start=mid+1
'''


'''
def call():
    a=10
    b=20
    a=a*b
    if a>b:
        print(a)
    pass

call()
'''
'''
s={1,2,34,5,6,2,1}
print(s)
s.add(10)
print(s)

#infrozen set size and element are immutable

'''

def sq(n):
    return n%2==0

a=list(map(sq,[1,2,3,4]))
#print(a)

a=list(map(lambda x: x*x,[1,2,3,4]))
#print(a)

a=list(filter(sq,[1,2,3,4,56]))
#print(a)

a=list(filter(lambda x: x%2==0 , [1,2,3,4,5,6,7,87,9]))
#print(a)
'''
from functools import reduce
print(2**3)
r=reduce(lambda x,y: x*x,[1,2,3,4,5])
print(r)
'''


# Python3 program to check for 
# balanced brackets. 

# function to check if 
# brackets are balanced 

#brackets=input("enter brackets")
'''
import re
a="kira 1 2 3 4stan mit "
x=re.findall('[a-z]+',a)
print(x)
x=re.findall('',a)
print(x)
'''
#stack
'''
class stack:
    
    def __init__(self):
        self.stack=[]
        
    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if len(self.stack)<0:
            print("no element left")
        else:
            temp=self.stack[-1]
            self.stack=self.stack[:-1]
            return temp
a=stack()
'''
#linked list
'''
class link():
    def __init__(self):
        self.value=[]
        self.adderss=[]
    
    def append():
        pass
    
    de remove():
        pass
    
    def insert():
        pass
    
    def search():
        pass
'''
def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()


a=input()
print(type(a))
    








































