def is_multiple(x, y) :
    if((x % y) == 0) :
        return(x,y,True)
    else :
        return(x,y,False)

result = is_multiple(6,2)

if(result[2] == True):
    print(str(result[0]) + " is a multiple of " + str(result[1]))
else :
    print(str(result[0]) + " is not a multiple of " + str(result[1]))