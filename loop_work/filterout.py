def filterout(arr):
    y = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    req = []
    for i in arr:
        for j in y:
            if i != j:
                req.append(i)
    return req
    

        
        
print( ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])
