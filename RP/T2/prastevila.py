# =============================================================================
# Praštevila
# =====================================================================@021945=
# 1. podnaloga
# Sestavite funkcijo `je_prastevilo`, ki sprejme število in vrne `True`, če 
# je podano število praštevilo, in `False`, če ni.
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
# =====================================================================@021946=
# 2. podnaloga
# Sestavite funkcijo `prastevilo(n)`, ki vrne `n`-to praštevilo.
# =============================================================================
def prastevilo(n):
    a = 0
    b = 1
    while a != n:
        if je_prastevilo(b):
            a += 1
        b += 1
    return b - 1
# =====================================================================@021947=
# 3. podnaloga
# Sestavite funkcijo `naslednje_prastevilo(n)`, ki vrne prvo praštevilo,
# strogo večje od števila `n`.
# =============================================================================
def naslednje_prastevilo(n):
    a = n+1
    while not (je_prastevilo(a)):
        a += 1
    return a
# =====================================================================@021948=
# 4. podnaloga
# Sestavite funkcijo `prvo_prastevilo_z_vsoto_stevk_vsaj(n)`, ki izračuna
# točno to, kar piše v njenem imenu.
# =============================================================================
def vsota_stevk(n):
    return sum([int(str(x)) for x in str(n)])

def prvo_prastevilo_z_vsoto_stevk_vsaj(n):
    a = 2
    while vsota_stevk(a) < n:
        a = naslednje_prastevilo(a)
    return a
