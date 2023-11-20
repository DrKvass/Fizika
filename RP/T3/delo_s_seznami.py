# =============================================================================
# Delo s seznami
# =====================================================================@021433=
# 1. podnaloga
# Sestavite funkcijo `razpolovi_seznam`, ki seznam prepolovi na dva podseznama
# in ju vrne kot par seznamov. V primeru lihe dolžine naj bo dolžina prvega
# podseznama krajša ali enaka dolžini drugega podseznama.
# 
#     >>> razpolovi_seznam(["a", "b", "c", "d"])
#     (["a", "b"], ["c", "d"])
#     >>> razpolovi_seznam([5, 4, 3, 2, 1])
#     ([5, 4], [3, 2, 1])
# =============================================================================
from math import trunc
from math import ceil



def razpolovi_seznam(n):
    n1 = n[:len(n)//2]
    n2 = n[len(n) // 2:]
    return(n1,n2)
# =====================================================================@021434=
# 2. podnaloga
# Sestavite funkcijo `zamenjaj_elementa(sez,i,j)`, ki iz seznama `sez` sestavi
# nov seznam, v katerem sta elementa na mestih `i` in `j` zamenjana med sabo.
# Če kateri od indeksov `i` in `j` ne ustrezata nobenemu elementu, naj funkcija
# vrne kar seznam `sez`.
# 
#     >>> zamenjaj_elementa([1, 2, 3, 4], 1, 2)
#     [1, 3, 2, 4]
#     >>> zamenjaj_elementa([1, 2, 3, 4], 3, 1)
#     [1, 4, 3, 2]
#     >>> zamenjaj_elementa([1, 2, 3, 4], 1, 2017)
#     [1, 2, 3, 4]
# =============================================================================
def zamenjaj_elementa(n, i, j):
    a = 0
    b = 0
    if i <= len(n) and j <= len(n):
        n[i], n[j] = n[j], n[i]
    return n
# =====================================================================@021435=
# 3. podnaloga
# Sestavite funkcijo `porezani_podseznami`, ki sprejme seznam in zgradi nov
# seznam podseznamov, ki jih pridobimo tako, da podanemu seznamu po vrsti
# odstranjujemo začetne elemente.
# 
#     >>> porezani_podseznami([1, 2, 3, 4])
#     [[1, 2, 3, 4], [2, 3, 4], [3, 4], [4], []]
# =============================================================================
def porezani_podseznami(n):
    a = []
    for i in range(len(n)+1):
        a.append(n[i:])
    return(a)
# =====================================================================@021436=
# 4. podnaloga
# Sestavite funkcijo `najvecji_element`, ki vrne največji element seznama. Če
# je seznam prazen, naj funkcija vrne `None`.
# 
#     >>> najvecji_element([2, 4, 3, 1])
#     4
#     >>> najvecji_element([1, 4, 5, 5, 2, -10])
#     5
# =============================================================================
from math import inf
def najvecji_element(n):
    if n != []:
        m = -999999
        for i in range(len(n)):
            a = n[i]
            if a > m:
                m = a
        return m
# =====================================================================@021437=
# 5. podnaloga
# Sestavite funkcijo `zdruzi_sezname`, ki zdruzi seznam seznamov v en seznam,
# ki vsebuje vse elemente seznamov v podanem seznamu seznamov.
# 
#     >>> zdruzi_sezname([[1], [2, 3], [4, 5, 6]])
#     [1, 2, 3, 4, 5, 6]
#     >>> zdruzi_sezname([[], [0], [], [0], [], [7], []])
#     [0, 0, 7]
# =============================================================================
def zdruzi_sezname(n):
    return [j for i in n for j in i]
