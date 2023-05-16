class Romen(object):
    def convert(selfs,x:str)->int:
        ROMAN={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        for i in range(len(x)-1):
            if ROMAN[x[i+1]]>ROMAN[x[i]]:
                total= total-ROMAN[x[i]]
            else:
                total=total+ROMAN[x[i]]
        total=total+ROMAN[x[i]]
        return total

