import math 

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    s1 = set(x)
    s2 = set(y)
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))

def cosine_sim(x, y):
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    elif len(x) != len(y) == 0:
        raise ValueError("lengths must be equal")
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(x)):
        val1 = x[i]
        val2 = y[i]
        sumxx += val1 * val1
        sumyy += val2 * val2
        sumxy += val1 * val2
    return sumxy/math.sqrt(sumxx*sumyy)

# Feel free to add more
