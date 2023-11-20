# =============================================================================
# Zlati rez
#
# Pravimo, da sta števili $a$ in $b$ v razmerju _zlatega reza_, kadar je
# $a : b$ enako $(a + b) : a$, kar je takrat, ko je $\frac{a}{b}$ enako
# številu $\phi = \frac{1 + \sqrt{5}}{2}$.
# 
# Približek števila $\phi$ lahko izračunamo z zaporedjem
#   $\phi_0, \phi_1, \phi_2, \dots$,
# kjer je $\phi_0 = 1$, naslednji približek $\phi_{n + 1}$ pa izračunamo
# kot
#   $\phi_{n + 1} = 1 + 1 / \phi_n$.
# =====================================================================@021475=
# 1. podnaloga
# Sestavite funkcijo `naslednji_priblizek`, ki iz podanega približka po
# zgornjem postopku izračuna naslednji približek števila $\phi$.
# =============================================================================
from cmath import sqrt

def naslednji_priblizek(f):
    return (1+ 1/f)
# =====================================================================@021476=
# 2. podnaloga
# Sestavite funkcijo `priblizek(k)`, ki izračuna `k`. približek števila
# $\phi$. Za začetni približek (ko je `k` enak $0$) vzamite število $1$.
# =============================================================================
def priblizek(k):
    f = 1
    for i in range(k):
        f = 1+1/f
    return(f)
# =====================================================================@021477=
# 3. podnaloga
# Sestavite funkcijo `natancni_priblizek`, ki sprejme pozitivno realno 
# število, ki predstavlja natančnost, ter izračuna prvi približek
# števila $\phi$, ki se od prejšnjega približka razlikuje za manj kot
# podano natančnost.
# =============================================================================
def natancni_priblizek(eps):
    p = 1
    n = naslednji_priblizek(p)
    while abs(p - n) >= eps:
        p = n
        n = naslednji_priblizek(p)
    return n
