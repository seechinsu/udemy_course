import math
def answer(h,q):
    solution = []
    list = []
    for i in range(1,h+1):
        list.append((2 ** i) - 1)
    top = max(list)
    print list
    print top
    for i in q:
        if i == top:
            solution.append(-1)
        elif i > (top - (len(list)-1)):
            solution.append(i+1)
        elif i in list:
            solution.append(min([x for x in list if x > i]))
        elif (i - max([x for x in list if x < i]))%max([x for x in list if x < i]) == 0:
            solution.append(max([x for x in list if x < i])*2+1)
        else:
            solution.append(int((math.ceil(float((i-max([x for x in list if x < i])))/3)*3)+max([x for x in list if x < i])))
    return solution
'''
print answer(3,7)
print answer(3,3)
print answer(3,5)
print answer(3,1)
print answer(5,19)
print answer(5,14)
print answer(5,28)
'''

#print answer(3,[7, 3, 5, 1])
#print answer(5,[19, 14, 28])
print answer(15,[24])