import math

def answer(h,q):
    count = 0
    q = q
    solution = []

    #print bin(q)
    #print bin(q<<1)
    #mask = (q<<1)-1
    #print bin(mask)
    #print bin((q & mask)+1)

    def clearbit(child, sumofdiff):
        mask = (child << 1) - 1
        newchild = (child & mask) + 1
        #print newchild
        return newchild, (sumofdiff + (child-newchild))

    while ((q+1)& q) !=0 and ((q+2) & (q+1)) !=0:
        q,count = clearbit(q,count)

        print q
        print count

    if ((q+1) & q) == 0:
        solution.append((2 * q) + 1 + count)
    elif ((q+2)&(q+1))==0:
        solution.append(q+1+count)

    #print ((q+1) & q)
    #print (q+2)&(q+1)

    print solution
    return None

answer(15,12)