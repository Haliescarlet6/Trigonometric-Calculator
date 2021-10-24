#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
print("Hello, Welcome To TRIGO HUB")
print("Here there are mainly three trigonometric function (sin,cos,tan) ignoring (cosec,sec,cot)")
usr = input("Which one do you need to find : " )




## SINE FUNCTION ##
if usr == "sin":
    n = int(input("Enter the value of the sin Function :"))
    userans = input("Do you want to find sin or cosec : ")

    if n < 90 :

        if n == 0 :
            out = 0 
        elif n == 30 :
            out = 1 / 2
        elif n == 45 :
            out = "1 / root2"
        elif n == 60 :
            out = "root3 / 2"
        elif n == 90 :
            out = "ND"

    else:
        r = (n % 90)
        q = n // 90 

        if q % 2 == 0 :

            if r == 0 :
                out  = (0)
            elif r == 30 :
                out = (0.5)
            elif r == 45 :
                out = ("1 / root2")
            elif r == 60 :
                out = ("root3 / 2 ")
            elif r == 90 :
                out = ("ND")

        else:
            if r == 90 :
                out = (0)
            elif r == 60 :
                out = (0.5)
            elif r == 45 :
                out =("1 / root2")
            elif r == 30 :
                out = ("root3 / 2 ")
            elif r == 0 :
                out = ("ND")

    if userans == "sin":
        out = out
        for i in range(1,10):
            if n > 0 and n < (90*i):
                print("+",out)
                break
            elif n  > (90*i) and n < (180*i):
                print("+",out)
                break
            elif n > (180*i) and n < (270*i):
                print("-",out)
                break
            elif n  > (270*i) and n < (360 *i):
                print("-",out)
                break
            else:
                pass
    elif userans == "cosec" :
        out = 1 / out
        for i in range(1,10):
            if n > 0 and n < (90*i):
                print("+",out)
                break
            elif n  > (90*i) and n < (180*i):
                print("+",out)
                break
            elif n > (180*i) and n < (270*i):
                print("-",out)
                break
            elif n  > (270*i) and n < (360 *i):
                print("-",out)
                break
            else:
                pass
            
            
## COSINE FUNCTION ##
elif usr == "cos":
    n = int(input("Enter the value of the sin Function :"))

    if n < 90 :

        if n == 90 :
            out = 0 
        elif n == 60 :
            out = 1 / 2
        elif n == 45 :
            out = "1 / root2"
        elif n == 30 :
            out = "root3 / 2"
        elif n == 0 :
            out = "ND"

    else:
        r = (n % 90)
        q = n // 90 

        if q % 2 == 0 :

            if r == 90 :
                out  = (0)
            elif r == 60 :
                out = (0.5)
            elif r == 45 :
                out = ("1 / root2")
            elif r == 30 :
                out = ("root3 / 2 ")
            elif r == 0 :
                out = ("ND")

        else:
            if r == 0 :
                out = (0)
            elif r == 30 :
                out = (0.5)
            elif r == 45 :
                out =("1 / root2")
            elif r == 60 :
                out = ("root3 / 2 ")
            elif r == 90 :
                out = ("ND")


    for i in range(1,10):
        if n > 0 and n < (90*i):
            print("+",out)
            break
        elif n  > (90*i) and n < (180*i):
            print("-",out)
            break
        elif n > (180*i) and n < (270*i):
            print("-",out)
            break
        elif n  > (270*i) and n < (360 *i):
            print("+",out)
            break
        else:
            pass
        
        
        
        
        
## TANGENT FUNCTION ##
    n = int(input("Enter the value of the tan Function :"))
    userans = input("Do you want to find the value of tan or cot : ")
    if n <= 90 :

        if n == 0 :
            out = 0 
        elif n == 30 :
            out = 1 / math.sqrt(3)
        elif n == 45:
            out = 1
        elif n == 60 :
            out = math.sqrt(3)
        elif n == 90 :
            out == "ND"

    if n > 90 :

        q = n // 90 
        r = n % 90 
        if q % 2 ==  0 :
            if r == 0 :
                out = 0 
            elif r == 30 :
                out = 1 / math.sqrt(3)
            elif r == 45:
                out = 1
            elif r == 60 :
                out = math.sqrt(3)
            elif r == 90 :
                out == "ND"

        else:
            if r == 90 :
                out = 0
            elif r == 600 :
                out = 1 / math.sqrt(3)
            elif r == 45:
                out = 1
            elif r == 30 :
                out = math.sqrt(3)
            elif r == 0 :
                out == "ND"


    if userans == "tan":

        out = out
        for i in range(1,10):

            if n > 0 and n < (90*i):
                print("+",out)
                break
            elif n  > (90*i) and n < (180*i):
                print("-",out)
                break
            elif n > (180*i) and n < (270*i):
                print("+",out)
                break
            elif n  > (270*i) and n < (360 *i):
                print("-",out)
                break
            else:
                pass

    elif userans == "cot":

        out = 1 / out 
        for i in range(1,10):

            if n > 0 and n < (90*i):
                print("+",out)
                break
            elif n  > (90*i) and n < (180*i):
                print("-",out)
                break
            elif n > (180*i) and n < (270*i):
                print("+",out)
                break
            elif n  > (270*i) and n < (360 *i):
                print("-",out)
                break
            else:
                pass
print("Thank You")
print("Please DO NOT USE DURING EXAMS!!!")


# In[ ]:




