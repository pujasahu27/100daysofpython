#string

"""def func():
    s=input("enter a string:")
    s+=''
    s2=''
    for i in range(len(s)-1,-1,-1):
      if(s[i]==s[i-1]):
        s2+="*"
      else:
        s2+=s[i]  
    print(s2[::-1])
func()          
    
def func():
    s1=input("enter a string 1:")
    s2=input("enter a string 2:")
    if(len(s1)!=len(s2)):
        return False
    for i in s1:
        if i not in s2:
            return False
    for i in s2:
        if i not in s1:
            return False    
    return True
a=func()
if(a):
    print('Anagram')
else:
    print('not Angaram')
    
def func():
    s=input("enter a sentence:")
    s1=s.strip()
    c=s1.count('')+1
    print("no of words:",c)
func()

import re
s="puja is nice girl"
s1=s.strip()
match=re.findall('',s1)
print(len(match)+1)

def func():
    s=input("enter a sring:")
    s1=''
    for i in range(-1,-len(s)-1,-1):
        s1+=l[i]
        s1+=''
    print(s1)
func()"""


def func():
    s=input("enter a sring:")
    s1=''
    l=s.split()
    for i in range(len(l)-1,-1,-1):
        s1+=l[i]
        s1+=''
    print(s1)
func()


# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")




    
