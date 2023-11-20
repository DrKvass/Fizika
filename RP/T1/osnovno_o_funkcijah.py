# =============================================================================
# Osnovno o funkcijah
# =====================================================================@022145=
# 1. podnaloga
# Definirajte funkcijo z imenom `funkcija`, ki ne sprejme argumentov in vrne
# poljubno celo število (`int`).
# =============================================================================
def funkcija():
    return 2
# =====================================================================@022146=
# 2. podnaloga
# Definirajte funkcijo z imenom `odmev`, ki sprejme en argument in ga vrne.
# =============================================================================
def odmev(a):
    return a
# =====================================================================@022147=
# 3. podnaloga
# Definirajte funkcijo z imenom `sestevek`, ki sprejme dva argumenta in vrne
# njuno vsoto.
# =============================================================================
def sestevek(a,b):
    return a+b
# =====================================================================@022148=
# 4. podnaloga
# Definirajte funkcijo z imenom `deljenje`, ki sprejme dve celi števili in vrne
# vrne dve vrednosti. Na prvem mestu vrne celoštevilski rezultat deljenja,
# na drugem pa ostanek pri deljenju. Zagotovljeno je, da druga vrednost ne bo `0`. 
# 
# Za vračanje več kot ene vrednosti po besedi `return` podate vrednosti ločene
# z vejico.
# =============================================================================
def deljenje(a,b):
    return (a//b, a%b)