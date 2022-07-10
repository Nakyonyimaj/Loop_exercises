# The very first one i created without importing a module
# def repeated(arr):

#     l = []
#     def remove_el(mylist,a):
#        mylist.remove(a)
#        return mylist


#     for  i in arr:

#         if str(remove_el(arr,i)).find(str(i)):
#             l.append(i)
        
        
#     return l
# print(repeated([2,4,3,8,4,3,2,8]))





# print(remove_el([2,4,3,8,4,3,2],4))
        


        

        

from collections import Counter
# A function that returns a list of numbers in a list that appear more than once

def repeated(arr):
    common = []
    count = Counter(arr)
    a = tuple(count.most_common())
    dct = dict((x,y) for x,y in a)
    for m , n in dct.items():
        if n > 1:
            common.append(m)
        
    return common


    
     

print(repeated([2,3,4,3,1,3,5,6,1,2,3]))
