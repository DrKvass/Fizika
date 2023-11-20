# =============================================================================
# Vsote potenc
# =====================================================================@021456=
# 1. podnaloga
# Sestavite funkcijo `vsota_prvih(n)`, ki vrne vsoto prvih `n` naravnih števil.
# =============================================================================
def vsota_prvih(n):
    a = 0
    while n > 0:
        a += n
        n = n-1
    return a
# =====================================================================@021457=
# 2. podnaloga
# Sestavite funkcijo `vsota_prvih_kvadratov(n)`, ki vrne vsoto kvadratov
# prvih `n` naravnih števil.
# =============================================================================
def vsota_prvih_kvadratov(n):
    a = 0
    while n > 0:
        a += n**2
        n = n - 1
    return a
# =====================================================================@021458=
# 3. podnaloga
# Sestavite funkcijo `vsota_prvih_potenc(n, k)`, ki vrne vsoto `k`-tih potenc
# prvih `n` naravnih števil. Argument `k` naj bo neobvezen in naj ima privzeto
# vrednost `1`.
# =============================================================================
def vsota_prvih_potenc(n, k=1):
    a = 0
    while n > 0:
        a += n**k
        n = n - 1
    return a
