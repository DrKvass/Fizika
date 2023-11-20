# =============================================================================
# Ogrevanje
# =====================================================================@021959=
# 1. podnaloga
# Nagajivi škrat je pokvaril zamike v funkciji `vsebuje_vprasaj` in premešal
# vrstice v funkciji `odstrani_presledke`. Popravite obe funkciji tako, da
# uspešno opravita vse teste.
# 
# *Funkciji sta že definirani v datoteki.*
# =============================================================================
def vsebuje_vprasaj(niz):
    for znak in niz:
        if znak == "?":
            return True
    return False

def odstrani_presledke(niz):
    nov_niz = ""
    for znak in niz:
        if not znak == " ":
            nov_niz += znak
    return nov_niz

# =====================================================================@021960=
# 2. podnaloga
# Napišite funkcijo `vsebuje_niz_z_vprasajem`, ki sprejme seznam nizov ter
# preveri, ali v seznamu obstaja niz, ki vsebuje vprašaj.
# 
#     >>> vsebuje_niz_z_vprasajem(['Katera', 'riba', 'bi', 'pa', 'ne', 'more?'])
#     True
#     >>> vsebuje_niz_z_vprasajem(['Skuša'])
#     False
# =============================================================================
def vsebuje_niz_z_vprasajem(n):
    for i in n:
        if vsebuje_vprasaj(i) == True:
            return True
    return False
# =====================================================================@021961=
# 3. podnaloga
# Sestavite funkcijo `zgolj_dolge_besede`, ki sprejme seznam nizov in število,
# ki predstavlja najmanjšo zahtevano dolžino niza, ter preveri, da so vsi nizi
# v seznamu primerne dolžine.
# 
#     >>> zgolj_dolge_besede(['Gandalf', 'Aragorn', 'Gimli', 'Legolas'], 5)
#     True
#     >>> zgolj_dolge_besede(['goblin', 'ork', 'zmaj', 'Balrog'], 5)
#     False
# =============================================================================
def zgolj_dolge_besede(n,k):
    for i in n:
        if len(i) < k:
            return False
    return True
