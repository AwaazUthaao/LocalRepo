from array import*

from string import*

# arrayname=array('i',[-1,1,4,3,4])
# moin=array('u',['V','A','N','S'])

# print (arrayname[0])
# print(moin[0])
# moin.append('S')
# print(moin.index('S'))
# print(moin)
# moin.remove('S')
# print(moin)
# moin.pop()
# print(moin)



a = array('u',['M','O','R','N','I','N','G'])
b = array('u',['G','O','O','D',' '])


b.extend(a)

print(b)

c = "moin"

b.fromunicode(c)

print(b)