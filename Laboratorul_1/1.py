#!usr/bin/python3

import sys

def calculateGreatesCommonDivisor(*arguments):
     if(len(arguments) == 0):
          return None
     greatest = 0
     first = arguments[0]
     for i in range(1, first + 1): # Deoarece cmmdc nu poate depăși primul număr
          gcd = True
          for j in arguments:
               if j % i != 0:
                    gcd = False
                    break
          if gcd == True:
               greatest = i
     return greatest

numbers = []
for i in sys.argv[1:]:
     numbers.append(int(i))

print("Cel mai mare divizor comun al numerelor este", calculateGreatesCommonDivisor(*numbers),sep=" : ")
               
        

          





