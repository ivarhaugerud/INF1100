def gamma1(t):
    if t < 5:
        return 0
    else:
        return 0.014

def gammaS(t):
    if t < 28:
        return 0
    else:
        return 0.0067

def gamma1(t):
    if 28 > t > 5:
        return 0.014
        
def alpha(t):
    if t < 5:
        return 0
    elif 28 > t > 4:
        return 0.0016
    else:
        return 0.006

def beta(t):
    if t < 5:
        return 0
    elif 28 > t > 4:
        return 0.0012
    else:
        return 0

def p(t):
    if t < 5:
        return 0
    else:
        return 1

def sigma(t):
    if t < 5:
        return 0
    else:
        return 20
