def answer(h,q):
    topconverter = (2**h)-1
    masks = [(2**i)-1 for i in range(1,h+1)]
    count = 0
    q = q
    solution = []

    def clearbit(child, sumofdiff):
        mask = max([x for x in masks if x < child])
        newchild = (child & mask) + 1
        #print bin(mask)
        #print bin(child)
        return newchild, (sumofdiff + (child-newchild))

    while ((q+1)& q) !=0 and ((q+2) & (q+1)) !=0:
        q,count = clearbit(q,count)

        #print q
        #print count

    if ((q+1) & q) == 0:
        if q == topconverter:
            solution.append(-1)
        else:
            solution.append((2 * q) + 1 + count)
        #print 'a'
    elif ((q+2)&(q+1))==0:
        solution.append(q+1+count)
        #print 'b'

    #print ((q+1) & q)
    #print (q+2)&(q+1)

    return solution

print answer(5,12)
print answer(5,19)
print answer(5,14)
print answer(5,28)

print answer(3,7)
print answer(3,3)
print answer(3,5)
print answer(3,1)

