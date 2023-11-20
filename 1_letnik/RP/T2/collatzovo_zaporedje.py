# =============================================================================
# Collatzovo zaporedje
#
# Collatzovo zaporedje tvorimo na sledeč način. Začnemo z nekim naravnim
# številom $n$, ki ga nato delimo z $2$, če je sodo, ali pa pomnožimo s $3$ in
# prištejemo $1$, če je liho. Postopek ponavljamo, dokler ne pridemo do števila
# $1$ (v tem primeru stvar ni več zanimiva, saj se začno ponavljati števila
# $1, 4, 2, 1, 4, 2, 1, \ldots$). Primer zaporedja, ki se začne z $6$ je tako
# $6, 3, 10, 5, 16, 8, 4, 2, 1$. Collatzova domneva, ki trdi, da za poljubno
# naravno število njegovo Collatzovo zaporedje sčasoma doseže $1$, je še vedno
# nerešena.
# =====================================================================@021468=
# 1. podnaloga
# Sestavite funkcijo `naslednji_clen`, ki sprejme število in izračuna člen,
# ki v Collatzovemu zaporedju sledi temu številu.
# =============================================================================
def naslednji_clen(m):
    if m % 2 == 0:
        return m / 2
    else:
        return 3 * m + 1

# =====================================================================@021469=
# 2. podnaloga
# Sestavite funkcijo `dolzina_zaporedja`, ki sprejme število in izračuna 
# dolžino Collatzovega zaporedja, ki se začne s tem številom.
# =============================================================================
def dolzina_zaporedja(m):
    a = 1
    while m > 1:
        m = naslednji_clen(m)
        a += 1
    return a

# =====================================================================@021470=
# 3. podnaloga
# Sestavite funkcijo `najvecji_clen`, ki sprejme število in izračuna največji 
# člen v Collatzovem zaporedju, ki se začne s tem številom.
# =============================================================================
def najvecji_clen(m):
    a = m
    while m > 1:
        m = naslednji_clen(m)
        if m > a:
            a = m
    return a

# =====================================================================@021471=
# 4. podnaloga
# Sestavite funkcijo `najdaljse_zaporedje(m, n)`, ki vrne dolžino najdaljšega
# zaporedja med vsemi tistimi Collatzovimi zaporedji, ki se začnejo s števili
# med (vključno) `m` in `n`.
# =============================================================================
def najdaljse_zaporedje(m, n):
    a = 0
    for i in range(m, n + 1):
        b = dolzina_zaporedja(i)
        if b > a:
            a = b
    return a
