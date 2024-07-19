#!usr/bin/python3

import sys


def convertString(s):
    n = len(s)

    for i in range(0,n):
        # print("Caracterul este : + ",s[i])
        # print("I ul este :",i)
        if(s[i].isupper() == True):
            # temp = s[i].lower()
            temp = "_" + s[i].lower()
            # print("Temp este : ", temp)
            temp_2 = s[i]
            s = s.replace(temp_2,temp)
            # print("String ul  schimbat este : ", s)
            # n = n + 1
            # print("N-ul este :", n) 
    return s

# Trebuie folosită o listă pentru  a parcurge pâna la final String-ul

n = sys.argv

if(len(n) != 2):
    print("Incorrect number of arguments !")
else:
    print(convertString(n[1]))