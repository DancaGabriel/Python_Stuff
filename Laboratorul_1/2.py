#!usr/bin/python3

import sys

def calculateVowels(input):
     sum = 0
     if(isinstance(input,str) == False):
          #input = str(input)
          return None
     n = len(input)
     for i in range(0,n):
          if(input[i] == "A" or input[i] == "E" or input[i] == "I" or input[i] == "O" or input[i] == "U" or
             input[i] == "a" or input[i] == "e" or input[i] == "i" or input[i] == "o" or input[i] == "u"):
               sum += 1
     return sum
    

n = sys.argv
if(len(n) == 1):
    print("You need to provide an String!")
elif len(n) > 2:
     print("Too many arguments given!")
else:
     print("The number of vowels is: ", calculateVowels(n[1]))