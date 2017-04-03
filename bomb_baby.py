def answer(M,F):
    mvalue = int(M)
    fvalue = int(F)
    cyclecount = 0

    if mvalue // fvalue > 2:
        cyclecount = (mvalue // fvalue)
        mvalue = mvalue - (fvalue * (mvalue // fvalue))
    elif fvalue // mvalue > 2:
        cyclecount = (fvalue // mvalue)
        fvalue = fvalue - (mvalue * (fvalue // mvalue))

    while mvalue != fvalue:
        if mvalue > fvalue:
            mvalue = mvalue - fvalue
            #print mvalue, "a"
            cyclecount += 1
        elif fvalue > mvalue:
            fvalue = fvalue - mvalue
            cyclecount += 1
            #print fvalue, "b"

    if mvalue != 1 and fvalue != 1:
        return "impossible"
    else:
        return str(cyclecount)

#print answer("2","1")
#print answer("4","7")
#print answer("2","4")
#print answer("50000001","2")
#print answer("4", "31")
