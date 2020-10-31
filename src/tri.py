def findcombo(vara,varb,varc):
    if vara + varb == varc:
        return(str(vara)+"+"+str(varb)+"="+str(varc))
    if vara - varb == varc:
        return(str(vara)+"-"+str(varb)+"="+str(varc))
    if vara/varb == varc:
        return(str(vara)+"/"+str(varb)+"="+str(varc))
    if vara*varb == varc:
        return(str(vara)+"*"+str(varb)+"="+str(varc))
    if vara == varb+varc:
        return(str(vara)+"="+str(varb)+"+"+str(varc))
    if vara == varb-varc:
        return(str(vara)+"="+str(varb)+"-"+str(varc))
    if vara == varb/varc:
        return(str(vara)+"="+str(varb)+"/"+str(varc))
    if vara == varb*varc:
        return(str(vara)+"="+str(varb)+"*"+str(varc))

var1,var2,var3 = [int(x) for x in input().split()]
print(findcombo(var1,var2,var3))