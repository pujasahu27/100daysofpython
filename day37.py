#finally keyword
"""try:
    l=[1,5,6,7]
    i=int(input("Enter the index:"))
    print(l[i])
except:
    print("some error occured")
finally:
    print("I am always executed")"""

def func1():
  try:
    l=[1,5,6,7]
    i=int(input("Enter the index:"))
    print(l[i])
    return 1
  except:
    print("some error occured")
    return 0
  finally:
    print("I am always executed")

x=func1()
print(x)
