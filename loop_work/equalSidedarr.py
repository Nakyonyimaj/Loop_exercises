#This function finds out if both sides of an array are equal
def equalSidearr(arr): 
    i = 0
    while i < len(arr):
#When you are standing at a postion i from the beginning of the array skip the value next to position i and sum up
#all the values after that value to the end of the array 
#Then compare the sum of the arr[:i+1] with that of arr[i+2:]

        
        if sum(arr[:i+1]) == sum(arr[i+2:]):
            print("The sum of both sides is:{}".format(sum(arr[:i+1])))
            print("The index at which both sides equate is : {}".format(i+1))
            break
            
        
        

        i = i + 1

equalSidearr([-1,-2,-3,-4,-3,-2,-1])       
    

      