#how import works in python
import math
result=math.sqrt(9)
print (result)

from math import sqrt
result=sqrt(9)
print (result)



from math import sqrt,pi
result=sqrt(9)*pi
print (result)

from math import *
result=sqrt(9)*pi
print (result)


import math as m
result=m.sqrt(9)*m.pi
print (result)

import math as math_builtin_python
result=math_builtin_python.sqrt(9)*math_builtin_python.pi
print (result)


import math
print(dir(math))
print(math.nan, type(math.nan))
print(math.ceil, type(math.ceil))
print(math.comb, type(math.comb))

from day44_2 import welcome,harry 
import math
print(dir(math))
print(math.nan, type(math.nan))
welcome()
print(harry)


import day44_2 as hr
import math
print(dir(math))
print(math.nan, type(math.nan))
hr.welcome()
print(hr.harry)
