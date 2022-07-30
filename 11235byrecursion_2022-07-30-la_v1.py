"Calculating the nth member of 11235 by recursion"

rvector = [1,1]

def recurf(nth):
    if nth >2:
        result = recurf(nth-2) + recurf(nth-1)
        rvector[nth] = result
    else:
        rvector == 0
    return rvector
    print(rvector)
