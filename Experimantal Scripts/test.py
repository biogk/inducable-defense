    k = np.arange(0, 40, 1)
    d = []
    i = 0
    for i in k:
        p = pow(math.e,-m)
        p = p * pow(m,i)
        q = p/math.factorial(i)
        d.append(q)
