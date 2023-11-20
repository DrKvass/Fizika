# =============================================================================
# Obresti
# =====================================================================@021419=
# 1. podnaloga
# Pri enostavnem obrestovanju s fiksno obrestno mero se vedno obrestuje
# samo glavnica, ne pa tudi obresti. Tako je vrednost na računu pri začetnem
# pologu $A_0$ po $n$ mesecih podana s formulo $A_0 (1 + m n)$, kjer je $m$
# pripadajoča mesečna obrestna mera.
# 
# Sestavite funkcijo
# `enostavno_obrestovanje(polog, mesecna_obrestna_mera, st_mesecev)`,
# ki za enostavno obrestovanju izračuna vrednost denarja na računu pri danem
# začetnem pologu, mesečni obrestni meri in številu mesecev.
# 
# Primeri:
# 
#     >>> enostavno_obrestovanje(100, 0.5, 0)
#     100.0
#     >>> enostavno_obrestovanje(100, 0.01, 1)
#     101.0
#     >>> enostavno_obrestovanje(100, 0.05, 12)
#     160.0
# =============================================================================
def enostavno_obrestovanje(polog, mesecna_obrestna_mera, st_mesecev):
    p = polog
    obm = mesecna_obrestna_mera
    mes = st_mesecev
    
    return p * (1+ obm*mes)
# =====================================================================@021420=
# 2. podnaloga
# Pri obrestno obrestnem računu s fiksno obrestno mero se poleg glavnice
# obrestujejo tudi obresti. Za glavnico $A_0$ je vrednost po $n$ mesecih podana
# s formulo $A_0 (1 + m)^n$, kjer je $m$ pripadajoča mesečna obrestna mera.
# 
# Sestavite funkcijo
# `obrestno_obrestovanje(polog, mesecna_obrestna_mera, st_mesecev)`,
# ki izračuna vrednost denarja na računu pri danem začetnem pologu, mesečni
# obrestni meri in številu mesecev, pri čemer se obresti računajo po obrestno
# obrestnem računu.
# 
# Primeri:
# 
#     >>> obrestno_obrestovanje(100, 0.5, 0)
#     100.0
#     >>> obrestno_obrestovanje(100, 0.05, 1)
#     105
#     >>> obrestno_obrestovanje(100, 0.01, 12)
#     112.68250301319698
# =============================================================================
def obrestno_obrestovanje(polog, mesecna_obrestna_mera, st_mesecev):
    p = polog
    obm = mesecna_obrestna_mera
    mes = st_mesecev
    
    return p * (1 + obm)**mes
# =====================================================================@021421=
# 3. podnaloga
# V bančništvu pogosto oglašujemo letno obrestno mero kljub temu, da obrestujemo
# mesečno.
# 
# Napišite funkcijo `pretvori_v_letno_obrestno_mero(mesecna_obrestna_mera)`,
# ki kot parameter sprejme mesečno obrestno mero, izraženo z decimalnim
# številom, in jo pretvori v letno obrestno mero, izraženo v odstotkih
# (zaokroženih na najbližje celo število). Pri računanju upoštevajte obrestno
# obrestni račun.
# 
# *Namig:* `help(round)`.
# =============================================================================

def pretvori_v_letno_obrestno_mero(mesecna_obrestna_mera):
    return round(100 * ((1+mesecna_obrestna_mera)**12) -100)
