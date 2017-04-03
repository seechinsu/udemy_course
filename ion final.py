import cProfile

def answer(h,q):
    masks = [(2**i)-1 for i in range(1,h+1)]
    topconverter = max(masks)
    solution = []

    for i in q:
        count = 0
        i = i
        def clearbit(child, sumofdiff):
            mask = max([x for x in masks if x < child])
            newchild = (child & mask) + 1
            return newchild, (sumofdiff + (child-newchild))

        while ((i+1)& i) !=0 and ((i+2) & (i+1)) !=0:
            i,count = clearbit(i,count)

        if ((i+1) & i) == 0:
            if i == topconverter:
                solution.append(-1)
            else:
                solution.append((2 * i) + 1 + count)
        elif ((i+2)&(i+1))==0:
            solution.append(i+1+count)

    return solution

print cProfile.run('answer(3,[7, 3, 5, 1])')