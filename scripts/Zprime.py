##------- Define Zprime function:

def ZPrime(a,b):
    ZP = 1 - (3 * (np.std(a) + np.std(b)) / abs(np.mean(a) - np.mean(b)))
    return ZP

ZP = ZPrime(a, b)
print(ZP)
