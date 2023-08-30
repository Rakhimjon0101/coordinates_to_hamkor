from xorazm import *

mylist = urganchDistrict

for i, val in enumerate(mylist):
    temp = val[0]
    mylist[i][0] = mylist[i][1]
    mylist[i][1] = temp


print('array [lat,long] \n%s ' % (mylist))

