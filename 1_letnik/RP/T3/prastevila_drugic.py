# =============================================================================
# Praštevila, drugič
# =====================================================================@021441=
# 1. podnaloga
# Definirajte funkcijo `je_deljivo_s_katerim_od(n, seznam)`, ki vrne `True`
# natanko tedaj, ko je število `n` deljivo z vsaj kakšnim številom iz seznama
# števil `seznam`.
# 
#     >>> je_deljivo_s_katerim_od(20, [3, 4, 6])
#     True
# =============================================================================

# število / elementom seznama = Z + r/elementom sez. -> št % el = 0

def je_deljivo_s_katerim_od(k, n):
    for i in n:
        if k % i == 0:
            return True
    return False
# =====================================================================@021442=
# 2. podnaloga
# Definirajte funkcijo `prastevila_do`, ki vrne seznam vseh praštevil, ki so
# manjša ali enaka podanemu številu.
# 
#     >>> prastevila_do(10)
#     [2, 3, 5, 7]
# =============================================================================
def prastevila_do(k):
    l = []
    for num in range(2, k + 1):
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    break
            else:
                l.append(num)
    return l
# =====================================================================@021443=
# 3. podnaloga
# Definirajte funkcijo `je_prastevilo`, ki vrne ali je število praštevilo.
# =============================================================================
def je_prastevilo(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False
    
    """if k == 2:
        return True
    elif k == 1:
        return False
    else:
        for i in range(2,int(k**(1/2))+1):
            if k % i == 0: 
                return False        
    return True"""
