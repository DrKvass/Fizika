# =============================================================================
# Kontrolne števke
# =====================================================================@021406=
# 1. podnaloga
# Sestavite funkcijo `vsota_kvadratov_stevk(n)`, ki vrne vsoto kvadratov števk
# *tromestnega* števila `n`.
# 
#     >>> vsota_kvadratov_stevk(123)
#     14
# =============================================================================
def vsota_kvadratov_stevk(n):
    n = str(n)
    return sum( [int(x)**2 for x in n] )
    

    

# =====================================================================@021407=
# 2. podnaloga
# Sestavite funkcijo `obrat(n)`, ki vrne število, ki ga dobimo, če tromestnemu
# številu `n` zamenjamo števki na mestu enic in stotic.
# 
#     >>> obrat(123)
#     321
# =============================================================================

def obrat(n):
    n = str(n)
    n = [str(x) for x in n]
    n.reverse()
    n = ''.join(n)
    return int(n)
    
    
    

# =====================================================================@021408=
# 3. podnaloga
# Da bi pri obdelavi podatkov lahko prepoznali morebitne napake, številske
# podatke pogosto opremimo s kontrolnimi števkami. Eden takšnih podatkov je
# sklic (referenca) po standardu SI12, ki ga uporabljamo pri plačevanju s
# položnicami UPN. Sklic zapišemo kot 13-mestno število, pri čemer je prvih 12
# števk poljubnih, zadnja (trinajsta) pa je kontrolna, torej izračunana iz
# prejšnjih, in nam služi za preverjanje, ali je pri branju podatkov s položnice
# bilo vse v redu.
# 
# Kontrolno števko za dano 12-mestno število izračunamo tako, da števke od desne
# proti levi pomnožimo z zaporednimi števili 2, 3, 4, … (enice torej pomnožimo z
# 2, desetice s 3, stotice s 4, …). Dobljene produkte seštejemo, nato izračunamo
# ostanek, ki ga da dobljena vsota pri deljenju z 11, in ta ostanek odštejemo od
# 11. Dobimo število med 1 in 11. Če je to število manjše od 10, je to že kar
# iskana kontrolna števka, sicer pa je kontrolna števka enaka 0.
# 
# Sestavite funkcijo `dodaj_kontrolno_stevko(sklic)`, ki za 12-mestno število
# `sklic` vrne 13-mestno število s pripadajočo kontrolno števko.
# 
#     >>> dodaj_kontrolno_stevko(265195368523)
#     2651953685235
# =============================================================================
def dodaj_kontrolno_stevko(sklic):
    m = sklic
    n = [str(x) for x in str(m)]
    r = [str(x) for x in str(m)]
    r.reverse()
    s = 0
    for i in range(len(n)):
        s = s + (i+2)*int(r[i])
    s = 11 - (s % 11)
    if -1 < s < 10:
        n.append(s)
    elif 10 <= s < 12:
        n.append("0")
    txt = ''.join(str(a) for a in n )
    return int(txt)