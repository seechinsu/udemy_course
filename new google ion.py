def answer(h,q):
    masks = [(2**i)-1 for i in range(1,h+1)]
    topconverter = max(masks)
    #count = 0
    #q = q
    solution = []

    for i in q:
        count = 0
        i = i
        def clearbit(child, sumofdiff):
            mask = max([x for x in masks if x < child])

            newchild = (child & mask) + 1
            #print bin(mask)
            #print bin(child)
            return newchild, (sumofdiff + (child-newchild))

        while ((i+1)& i) !=0 and ((i+2) & (i+1)) !=0:
            i,count = clearbit(i,count)

            #print i
            #print count

        if ((i+1) & i) == 0:
            if i == topconverter:
                solution.append(-1)
            else:
                solution.append((2 * i) + 1 + count)
            #print 'a'
        elif ((i+2)&(i+1))==0:
            solution.append(i+1+count)
            #print 'b'

        #print ((i+1) & i)
        #print (i+2)&(i+1)

    return solution

print answer(3,[7, 3, 5, 1])
print answer(5,[19, 14, 28])

# print answer(5,12)
# print answer(5,19)
# print answer(5,14)
# print answer(5,28)
# print answer(3,7)
# print answer(3,3)
# print answer(3,5)
# print answer(3,1)



