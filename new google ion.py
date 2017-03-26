import math

def answer(h,q):
    solution = []

    #print bin(q)
    #print bin(q<<1)
    #mask = (q<<1)-1
    #print bin(mask)
    #print bin((q & mask)+1)

    def clearbit(child):
        mask = (child << 1) - 1
        newchild = (child & mask) + 1
        print newchild
        sumofdiff += child-newchild
        return newchild, sumofdiff



    while ((q+1)& q) !=0 and ((q+2) & (q+1)) !=0:
        q = clearbit(q)

        print sum
        #if ((newq+1) & newq) == 0:
        #    solution.append[(2 * newq) + 1 + sumofdiff]
        #elif ((newq+2)&(newq+1))==0:
        #    solution.append[newq+1+sumofdiff]

    return None

answer(15,12)