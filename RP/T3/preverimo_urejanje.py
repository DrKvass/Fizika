# =============================================================================
# Preverimo urejanje
# =====================================================================@021963=
# 1. podnaloga
# Z namenom preverjanja različnih algoritmov za urejanje seznamov, si želite
# pripraviti zanimive testne primere. Ti bodo sestavljeni iz seznamov parov, 
# kjer druga komponenta pove, na katerem mestu mora stati par. 
# 
# Sestavite funkcijo `pripravi_primer`, ki sprejme dva seznama - seznam 
# elementov in seznam indeksov - ter iz njiju napravi testni primer. 
# 
#     >>> pripravi_primer(["c", "b", "d", "a"], [2, 1, 3, 0])
#     [('c', 2), ('b', 1), ('d', 3), ('a', 0)]
#     >>> pripravi_primer(['daj', 'cas', 'da', 5, 'zapeljem', 'mi', 'te', 'minut'],[3, 4, 5, 0, 7, 2, 6, 1])
#     [('daj', 3), ('cas', 4), ('da', 5), (5, 0), ('zapeljem', 7), ('mi', 2), ('te', 6), ('minut', 1)]
# =============================================================================
def pripravi_primer(n, m):
    return list (zip(n,m))
# =====================================================================@021964=
# 2. podnaloga
# Svoje urejevalne algoritme ste uporabili na primerih in želite preveriti,
# ali delujejo pravilno. Sestavite funkcijo`pravilno_urejen`, ki pove, ali je
# seznam urejen skladno z zgornjim principom.
# 
# Namig: uporabite funkcijo `enumerate`
# 
#     >>> pravilno_urejen([('so', 5), ('vcasih', 6), ('stezice', 3), ('bile?', 7), ('tiste', 2), ('k', 4), ('Kje', 0), ('so', 1)])
#     False
#     >>> pravilno_urejen([('Kje', 0), ('so', 1), ('tiste', 2), ('stezice', 3), ('k', 4), ('so', 5), ('vcasih', 6), ('bile?', 7)])
#     True
#     >>> pravilno_urejen([('daj', 3), ('cas', 4), ('da', 5), (5, 0), ('zapeljem', 7), ('mi', 2), ('te', 6), ('minut', 1)])
#     False
#     >>> pravilno_urejen([(5, 0), ('minut', 1), ('mi', 2), ('daj', 3), ('cas', 4), ('da', 5), ('te', 6), ('zapeljem', 7)])
#     True
# =============================================================================
def pravilno_urejen(n):
    for i, v in enumerate(n):
        if i != v[1]:
            return False
    return True
