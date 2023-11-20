#------------------------------ INFO ------------------------------# 
# Author: Luka Orlić
# Date made: 17.11.2023
# Date last updated: 20.11.2023
# Version: 2.0
# Lol feel free to use this i guess
#----------------------------- Imports ----------------------------#

import statistics as st
import numpy as np
import uncertainties as un
from uncertainties import ufloat
from uncertainties.umath import *
from decimal import *

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Iz seznama sestavi ufloat tip za uporabo v "dictionary"-ju
def SeznamMeritev(l, tag):
    return ufloat(st.mean(l), st.stdev(l)/sqrt(len(l)), tag)
# Uredi lep izgled natisnjenih matrik
def matrix_print(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    print()
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

var = {
    
"R"   : ufloat( 2.123*10**(-3) , 1*10**(-6), "R" )           ,
"D"   : ufloat( 4.15*10**(-3) , 2.4*10**(-4)*10**(-3), "D" ) ,
"l"   : ufloat( 999.12*10**(-3) , 0.0058*10**(-3) , "l" )    ,
"primer 1"  : ufloat( 0 , 0 , "primer 1" )                   ,
"primer 2"  : SeznamMeritev([0,0], "primer 2")

} #EDIT

# Dodajanje novih meritev:

'''
Za dodajanje novih meritev morate v tako imenovani 'dictionary' z imenom "var" dodati nov element.
Nov element doate tako da v novo vrstico napišete:

prvi primer :

"<ime spremenljivke>" : ufloat( <vrednost meritve> , <absolutna napaka> , "<ime spremenljivke>" )

drugi primer (uporabite le če ima seznam  [<meritve ločene z vejco>] NAJMANJ dve (2) vrednosti!) :

"<ime spremenljivke>" : SeznamMeritev( [<meritve ločene z vejco>] , <ime spremenljivke> )

Tukaj spremenite vse vrednosti znotraj <teh (špicastih) oklepajev> na željene vrednosti.
----> !!! Ne pozabite na to predzadnji vrstici dodati vejco !!! <----
'''

# Vpiši funkcijo, ki uporablje "mX" in "fX"... npr:

primer2 = var["primer 2"] 

rezultat = np.pi*var["R"]*var["D"]*var["D"]/4/var["l"]  + 0*var["primer 1"] + 0*primer2 #EDIT

'''
za poljubno spremenljivko lahko uporabit bodisi var["<ime spremenljivke>"] bodisi naredite posebno vrstico

<ime spremenljivke> = var["<ime spremenljivke>"] ter uporabljate <ime spremenljivke>

UPORABITI MORATE VSE SPREMENLJIVKE -> ČE TEGA NE ŽELITE STORITI DODAJTE NA KONEC : 
0*(var["<ime neuporavbljene spremenljivke 1>"]) + 0*(var["<ime neuporavbljene spremenljivke 2>"])
IN TAKO NAPREJ ZA VSE NEUPORABLJENE SPREMENLJIVKE!!!
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zamenjaj s "True" če hočeš da ti izpiše rezultate tudi v LaTeX kodi... (ni vse lahko pa pomaga)
latex_print = False

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Pripravi seznam vseh ufloat-ov potrebnih za konstrukcijo matrik
seznam = []
for i in var:
    seznam = seznam + [var[i]]
seznam = seznam + [rezultat]

# Konstruira matrike
array_cov = un.covariance_matrix(seznam)
array_cor = un.correlation_matrix(seznam)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Izpis rezultatov programa

print("----------------------------------------------------------------------------------------------------------------------------------------\nVhodni podatki : \n")
for i in var:
    print(repr(var[i]))
print("----------------------------------------------------------------------------------------------------------------------------------------\nObčutljivostni koeficient : \n")
for i in var:
    print(i + " : " + str(abs(rezultat.derivatives[var[i]])))
print("----------------------------------------------------------------------------------------------------------------------------------------\nPrispevek negotovosti : \n")
for (var, error) in rezultat.error_components().items():
    print( "{}: {}".format(var.tag, error))
print("----------------------------------------------------------------------------------------------------------------------------------------\nmatrike se zapišejo v isti vrsti kot spremenljivke v 'dictionary'-ju torej prvi stolpec predstavlja prvo zapisano vrednost kakor tudi prva vrstica predstavlja prvo zapisano vrednost.\n----------------------------------------------------------------------------------------------------------------------------------------\nCorrelation matrix : \n")
matrix_print(array_cor)
print("----------------------------------------------------------------------------------------------------------------------------------------\nCovariance matrix : \n")
matrix_print(array_cov)
print("----------------------------------------------------------------------------------------------------------------------------------------\nRezultat : " + str(repr(rezultat)) + "\n" + "95% prepričanost : " + str(rezultat.s*2) + "\n\n\n") #"{:.3u}".format
if latex_print:
    print("---LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print---\n----------------------------------------------------------------------------------------------------------------------------------------\nVhodni podatki : \n")
    for i in var:
        print(repr("{:L}".format(var[i])))
    print("----------------------------------------------------------------------------------------------------------------------------------------\nRezultat : " + str("{:L}".format(rezultat)) + "\n\n---LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print-LaTeX print---")
