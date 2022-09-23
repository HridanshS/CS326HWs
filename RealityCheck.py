import math

if __name__ == "__main__":
    m = []
    n = 0
    s = []


    if (n==0):
        m.insert(n, 0)
        s.insert(n, m[n])

    n = 1
    while ( (2 * s[n-1]) >= (m[n-1])):
        if (n <= 1):
            m.insert(n, 0)
        else:
            insertValM_lower = int(math.floor(n/2.0))
            insertValM_upper = int(math.ceil(n/2.0))
            insertElemM = (m[insertValM_lower] + m[insertValM_upper] + n-1)
            m.insert(n, insertElemM)

        if (n < 140):
            s.insert(n, m[n])
        else:
            insertValS_low = 6+int(math.floor((7*n)/10.0))
            insertValS_up = 6*(int(math.ceil(n/5.0)))
            insertValS_up2 = int(math.ceil(n/5.0))
            insertElemS = insertValS_up + s[insertValS_up2] + s[insertValS_low]
            s.insert(n, insertElemS)
        n += 1

    print(f"Last element index: {n-1}")
    print(f"Last element of S[N]: {s[n-1]}; Last element of M[N]: {m[n-1]}")