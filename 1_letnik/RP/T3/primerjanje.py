# =============================================================================
# Primerjanje
#
# Pri reševanju nalog ne uporabljajte funkcij kot sta `min` in `max`.
# =====================================================================@021438=
# 1. podnaloga
# Definirajte funkcijo `vecji_element`, ki sprejme seznam in število ter kot
# rezultat vrne, ali seznam vsebuje število strogo večje od podanega.
# 
#     >>> vecji_element([3, 6, 2], 5)
#     True
#     >>> vecji_element([7, 5, 1], 8)
#     False
#     >>> vecji_element([3], 3)
#     False
# =============================================================================
def vecji_element(n, k):
    for i in n:
        if i > k:
            return True
    return False
# =====================================================================@021439=
# 2. podnaloga
# Definirajte funkcijo `prvi_najvecji`, ki kot rezultat vrne `True`, če je prvi
# element seznama večji ali enak preostalim elementom seznama, in `False`
# sicer.
# 
#     >>> prvi_najvecji([5, 3, 6, 2])
#     False
#     >>> prvi_najvecji([8, 7, 5, 1])
#     True
# =============================================================================
def prvi_najvecji(n):
    for i in n: 
        if i > n[0]:
            return False
    return True
# =====================================================================@021440=
# 3. podnaloga
# Definirajte funkcijo `vsi_vecji(sez1, sez2)`, ki sprejme dva seznama, `sez1`
# in `sez2`, ter preveri ali je vsak element seznama `sez1` večji ali enak
# elementom seznama `sez2`.
# 
#     >>> vsi_vecji([2, 4], [1, 3])
#     False
#     >>> vsi_vecji([5, 8], [1, 2, 4])
#     True
# =============================================================================
def vsi_vecji(n, m):
    for j in range(len(m)):
        for i in range(len(n)):
            if  n[i] < m[j]:
                return False
    return True
