# =============================================================================
# Vsote števk
# =====================================================================@021459=
# 1. podnaloga
# Sestavite funkcijo `vsota_stevk(n)`, ki vrne vsoto števk podanega števila.
# =============================================================================
def vsota_stevk(n):
    return sum([int(str(x)) for x in str(n)])
# =====================================================================@021460=
# 2. podnaloga
# Sestavite funkcijo `vsota_vecjih_stevk(n, k)`, ki vrne vsoto tistih števk
# števila `n`, ki so večje ali enake `k`. Če parametra `k` ne podamo, naj
# funkcija vrne vsoto vseh števk števila `n`.
# =============================================================================
def vsota_vecjih_stevk(n, k=(0)):
    return sum([int(x) for x in str(n) if int(x) >= k])
# =====================================================================@021461=
# 3. podnaloga
# Sestavite funkcijo `vsota_stevk_stevil_med(m, n)`, ki vrne vsoto števk
# vseh števil med vključno `m` in `n`.
# =============================================================================
def vsota_stevk_stevil_med(m, n):
        s = 0
        for i in range(m, n+1):
            s += vsota_stevk(i)
        return s