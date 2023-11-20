# =============================================================================
# Delo z nizi
# =====================================================================@021444=
# 1. podnaloga
# Sestavite funkcijo `prezrcali`, ki vrne prezrcaljen niz.
# 
#     >>> prezrcali('abeceda')
#     'adeceba'
# =============================================================================
def prezrcali(n):
    return n[::-1]
# =====================================================================@021445=
# 2. podnaloga
# Sestavite funkcijo `je_palindrom`, ki preveri, če je niz palindrom.
# 
#     >>> je_palindrom('kajak')
#     True
# =============================================================================
def je_palindrom(a):
    if a == prezrcali(a): return True 
    else: return False
# =====================================================================@021446=
# 3. podnaloga
# Sestavite funkcijo `odstrani_presledke`, ki sprejme niz in vrne nov niz, ki
# ga dobimo, če iz podanega niza odstranimo vse presledke.
# 
#     >>> odstrani_presledke('Ni vsak dan nedelja')
#     'Nivsakdannedelja'
# =============================================================================
def odstrani_presledke(n): return n.replace(" ","")
# =====================================================================@021447=
# 4. podnaloga
# Napišite funkcijo `odstrani_ponovljene_presledke`, ki sprejme niz in vrne nov
# niz, kjer večkratne ponovitve presledka zamenjamo z enojnim presledkom.
# 
#     >>> odstrani_ponovljene_presledke('  * -   *   - * ')
#     ' * - * - * '
# =============================================================================
import re
def odstrani_ponovljene_presledke(n): 
    return re.sub(" +", " ", n)
# =====================================================================@021448=
# 5. podnaloga
# Na zabavi ste uspeli dobiti telefonsko številko sošolke/sošolca, ki ste jo/ga
# pecali cel večer. Toda na poti domov vam je dež zbrisal nekaj cifer, zato ste
# vdrli v FMF bazo in pridobili seznam vseh telefonskih številk.
# 
# Napišite funkcijo `najdi_stevilko(vzorec, seznam)`, ki iz možnega seznama
# telefonskih številk vrne seznam tistih, ki ustrezajo vzorcu. Telefonske
# številke so podane kot nizi z 9 znaki iz števk `0`-`9`, vzorec pa vsebuje
# tudi znak `*`, ki pomeni, da te števke ne poznamo.
# 
# **Namig:** Napišite pomožno funkcijo, ki preveri ali številka ustreza vzorcu.
# 
#     >>> najdi_stevilko('05123***6', ['041890343', '051234446', '051342236'])
#     ['051234446']
#     >>> najdi_stevilko('0********', ['041890343', '051234446', '051342236'])
#     ['041890343', '051234446', '051342236']
#     >>> najdi_stevilko('0*1123*57', ['041123457', '071123456', '051123457'])
#     ['041123457', '051123457']
# =============================================================================
def najdi_stevilko(k, n):
    for i in n:
        if i in n:
            for j in range(len(k)):
                if k[j] != i[j] and k[j] != "*":
                    n.remove(i)
                    break
    return n
