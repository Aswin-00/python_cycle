#!/bin/python3

import math
import os
import random
import re
import sys

'''
Neo has a complex matrix script. The matrix script is a  X  grid of strings.
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).


7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

'''


m=['tsi','h%x','i #','sM ','$a ' ,'#t%','ir!']
##
##first_multiple_input = input().rstrip().split()
##
##n = int(first_multiple_input[0])
##
##m = int(first_multiple_input[1])
##
##matrix = []
##
##for _ in range(n):
##    matrix_item = input()
##    matrix.append(matrix_item)
##
##a=''
##for i in range(n):
##    a=i+a

        

sample=''
patter='!,@,#,$,%,&'
for i   in range(0,3):
    for j in range(0,7):
        print(f'm{j}{i} == {m[j][i]}')
        sample+=(m[j][i])

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))

        







