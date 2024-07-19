#!usr/bin/python3

import sys

def compareStrings(s1,s2):
    sum = 0
    length = len(s1)
    while True:
        index =  s2.find(s1)
        if(index == -1):
            break
        else:
            sum += 1
            list1 = list(s2)
            temp = "?" * length 
            list1[index:index+length] = temp
            s2 = ''.join(list1)
            # print(s2)
    return sum

    
n = sys.argv
if(len(n) != 3):
    print("Incorrect number of parameters")
else:
    print(compareStrings(n[1],n[2]))





