"Calculating the nth member of 11235 by recursion"
def recurf(nth):
    result = 1
    if nth >2:
        result = recurf(nth-2) + recurf(nth-1)
        #print(result)
        #list rvector[]
        #rvector[nth] = result
    else:
        result = 1
        #rvector = 1
    print(result)
    return result
    #return rvector
print(recurf(5))

print("\n\nOnko tää tämä ? Recursion Example Results")
recurf(5)