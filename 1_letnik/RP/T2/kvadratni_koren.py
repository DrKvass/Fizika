# =============================================================================
# Kvadratni koren
#
# Približke za kvadratni koren števila $n$ lahko izračunamo po naslednjem
# postopku. Začetni približek $x_0$ je enak $n / 2$. Vsak naslednji približek
# $x_{k + 1}$ pa izračunamo kot $(x_k + n / x_k) / 2$.
# =====================================================================@021462=
# 1. podnaloga
# Sestavite funkcijo `priblizek_po_korakih(n, k)`, ki po zgornjem postopku
# izračuna `k`. približek korena števila `n`.
# =============================================================================
def priblizek_po_korakih(n, k):
    x = n/2
    for i in range(k):
        x = (x + n/x)/2
    return x
# =====================================================================@021463=
# 2. podnaloga
# Sestavite funkcijo `priblizek_do_natancnosti(n, eps)`, ki po zgornjem
# postopku izračuna prvi približek korena števila `n`, za katerega se kvadrat
# približka od `n` razlikuje za manj kot `eps`. Smislena vrednost za argument
# `eps` je npr. $10^{-6}$.
# =============================================================================
def priblizek_do_natancnosti(n, eps):
    x = n/2
    while not(abs(x*x-n)<eps):
        x = (x + n/x)/2
    return x
