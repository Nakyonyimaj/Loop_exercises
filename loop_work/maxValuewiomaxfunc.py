#finds the min and max without using the min() and max() functions
def max_min(arr):
    great = set()
    less = set()
    not_want =[]
    want = []

#this for loop is going to enable us compare each value in the list with all the others
#so will be all values that have values that they are greater than 
#hence the one missing is the lowest
    for i in arr :
        for j in arr:
            if i > j:
                great.add(j)
                want.append(i) 

#this for loop is going to enable us compare each value in the list with all the others
#so this will have  all values that have values that they are less than 
#hence the one missing is the greatest 
        for m in arr:
            if i < m:
                less.add(m)
                not_want.append(i)

    my_max =  set(want) - set(not_want)
    my_min = set(not_want) - set(want)
# Note that both the lists want & not_want are turned into sets because they have muitiply values that are similar
#But since sets dont allow repeation of items ,they become more convenient to use 

    return '{} = maximum'.format(my_max) , '{} = minimum'.format(my_min)
    

max_min([2,3,5,0,1,8,-1,-5])
