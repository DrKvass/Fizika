# =============================================================================
# Delne vsote vrst
# =====================================================================@021951=
# 1. podnaloga
# Napišite funkcijo `vsota_potenc(n, k)`, ki izračuna vsoto
#    $$1^k + 2^k + ... + n^k$$
# =============================================================================
def vsota_potenc(n,k):
    a = 0
    for i in range(n):
        a += (n-i)**k
    return a
# =====================================================================@021952=
# 2. podnaloga
# Sestavite funkcijo `vsota_harmonicne(n)`, ki izračuna delno vsoto
#    $$1 + 1 / 2 + 1 / 3 + ... + 1 / n$$
# =============================================================================
def vsota_harmonicne(n):
    a = 0
    for i in range(n):
        a += 1/(n-i)
    return a
# =====================================================================@021953=
# 3. podnaloga
# Sestavite funkcijo `divergenca_harmonicne(n)`, ki izračuna število
# členov harmonične vrste, ki jih je treba sešteti, da bo njihova delna
# vsota večja od števila `n`.
# =============================================================================
def divergenca_harmonicne(n):
    s = 1
    a = 0
    while a < n:
        a += 1/s
        s += 1
    return s - 1
# =====================================================================@021954=
# 4. podnaloga
# Sestavite funkcijo `eksponentna(n)`, ki izračuna delno vsoto:
#    $$1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / n!$$
# =============================================================================
import math
def eksponentna(n):
    a = 1
    for i in range(n):
        a += 1/(math.factorial(n-i))
    return a 
