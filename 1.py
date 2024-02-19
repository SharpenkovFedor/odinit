b = int(input())
c = int(input())
d = int(input())
ctxt = str(c)
dtxt = str(d)
cdtxt = ctxt + "." + dtxt
cddig = float(cdtxt)
a = b * cddig
print (a)
dctxt = dtxt + ctxt
dcdig = int(dctxt)
print (dcdig)
if dcdig > a:
    print ('ДА')
else:
    print ('НЕТ')