import operator
def answer(xs):

    newxs = [x for x in xs if x!=1 and x!=0]

    if len(xs) == len([x for x in xs if x==0]):
        product = '0'
    elif len(xs)!=1 and len(xs) == (len([x for x in xs if x==0]) + len([x for x in xs if x < 0])) and len([x for x in xs if x < 0]) ==1:
        product = '0'
    elif len([x for x in xs if x < 0]) % 2 != 0 and len([x for x in xs if x < 0]) != 0 and len([x for x in xs if x < 0]) != 1:
        newxs.remove((max(x for x in xs if x < 0)))
        product = str(reduce(operator.mul, newxs, 1))
    elif len([x for x in xs if x < 0]) == 1:
        product = str(newxs[0])
    else:
        product = str(reduce(operator.mul, newxs, 1))

    return product

print answer([2, 0, 2, 2, 0])
print answer([-2, -3, 4, -5])
print answer([-2, -3, -5, -5])
print answer([-2])
print answer([0,0,1,0,0])
print answer([0,0,0,0])
print answer([0,0,-2,0])
print answer([0,0,-2,0,-2])
print answer([0,0,-2,0,-2,-2,-2])