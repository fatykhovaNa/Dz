# -*- coding:utf -8 -*-
#!/usr/bin/python3

import random
import math

num1 = list(input())
num2 = list(input())
num3 = num1
num4=list(filter(lambda x:x in num1, num2))
num3=num3+num4
print (num3)


