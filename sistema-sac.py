import pandas as pd

vPrincipal = float(input("Valor principal: "))
nParcela = float(input("Numero de parcelas: "))
amortizacao = round(vPrincipal / nParcela, 2)
p = 1
taxa = float(input("Valor da taxa: "))
pc = taxa/100
tMensal = round((1 + pc)**(1/12) - 1, 6)
juro = round((nParcela - p + 1) * amortizacao * tMensal, 3)
prestacao = round(amortizacao + juro, 2)
vFinal = vPrincipal - amortizacao

vPrincipal2 = vFinal
nParcela2 = nParcela - 1
amortizacao2 = round(vFinal / nParcela2, 2)
juro2 = round((nParcela2 - p + 1) * amortizacao2 * tMensal, 3)
prestacao2 = round(amortizacao2 + juro2, 2)
vFinal2 = vPrincipal2 - amortizacao2

vPrincipal3 = vFinal2
nParcela3 = nParcela2 - 1
amortizacao3 = round(vFinal2 / nParcela3, 2)
juro3 = round((nParcela3 - p + 1) * amortizacao3 * tMensal, 3)
prestacao3 = round(amortizacao3 + juro3, 2)
vFinal3 = vPrincipal3 - amortizacao3

vPrincipal4 = vFinal3
nParcela4 = nParcela2 - 1
amortizacao4 = round(vFinal3 / nParcela4, 2)
juro4 = round((nParcela4 - p + 1) * amortizacao4 * tMensal, 3)
prestacao4 = round(amortizacao4 + juro4, 2)
vFinal4 = vPrincipal4 - amortizacao4

vPrincipal5 = vFinal4
nParcela5 = nParcela2 - 1
amortizacao5 = round(vFinal4 / nParcela5, 2)
juro5 = round((nParcela5 - p + 1) * amortizacao5 * tMensal, 3)
prestacao5 = round(amortizacao5 + juro5, 2)
vFinal5 = vPrincipal5 - amortizacao5

vPrincipal6 = vFinal5
nParcela6 = nParcela2 - 1
amortizacao6 = round(vFinal5 / nParcela6, 2)
juro6 = round((nParcela6 - p + 1) * amortizacao6 * tMensal, 3)
prestacao6 = round(amortizacao6 + juro6, 2)
vFinal6 = vPrincipal6 - amortizacao6

vPrincipal6 = vFinal5
nParcela6 = nParcela2 - 1
amortizacao6 = round(vFinal5 / nParcela6, 2)
juro6 = round((nParcela6 - p + 1) * amortizacao6 * tMensal, 3)
prestacao6 = round(amortizacao6 + juro6, 2)
vFinal6 = vPrincipal6 - amortizacao6

vPrincipal7 = vFinal6
nParcela7 = nParcela2 - 1
amortizacao7 = round(vFinal6 / nParcela7, 2)
juro7 = round((nParcela7 - p + 1) * amortizacao7 * tMensal, 3)
prestacao7 = round(amortizacao7 + juro7, 2)
vFinal7 = vPrincipal7 - amortizacao7

vPrincipal8 = vFinal7
nParcela8 = nParcela2 - 1
amortizacao8 = round(vFinal7 / nParcela8, 2)
juro8 = round((nParcela8 - p + 1) * amortizacao8 * tMensal, 3)
prestacao8 = round(amortizacao8 + juro8, 2)
vFinal8 = vPrincipal8 - amortizacao8

vPrincipal9 = vFinal8
nParcela9 = nParcela2 - 1
amortizacao9 = round(vFinal8 / nParcela9, 2)
juro9 = round((nParcela9 - p + 1) * amortizacao9 * tMensal, 3)
prestacao9 = round(amortizacao9 + juro9, 2)
vFinal9 = vPrincipal9 - amortizacao9

vPrincipal10 = vFinal9
nParcela10 = nParcela2 - 1
amortizacao10 = round(vFinal9 / nParcela10, 2)
juro10 = round((nParcela10 - p + 1) * amortizacao10 * tMensal, 3)
prestacao10 = round(amortizacao10 + juro10, 2)
vFinal10 = vPrincipal10 - amortizacao10

vPrincipal11 = vFinal10
nParcela11 = nParcela2 - 1
amortizacao11 = round(vFinal10 / nParcela11, 2)
juro11 = round((nParcela11 - p + 1) * amortizacao11 * tMensal, 3)
prestacao11 = round(amortizacao11 + juro11, 2)
vFinal11 = vPrincipal11 - amortizacao11

vPrincipal12 = vFinal11
nParcela12 = nParcela2 - 1
amortizacao12 = round(vFinal11 / nParcela12, 2)
juro12 = round((nParcela12 - p + 1) * amortizacao12 * tMensal, 3)
prestacao12 = round(amortizacao12 + juro12, 2)
vFinal12 = vPrincipal12 - amortizacao12



d = [ [vPrincipal, prestacao, amortizacao, juro, vFinal],
     [vFinal, prestacao2, amortizacao2, juro2, vFinal2],
     [vFinal2, prestacao3, amortizacao3, juro3, vFinal3],
     [vFinal4, prestacao4, amortizacao4, juro4, vFinal4],
     [vFinal5, prestacao5, amortizacao5, juro5, vFinal5],
     [vFinal6, prestacao6, amortizacao6, juro6, vFinal6],
     [vFinal7, prestacao7, amortizacao7, juro7, vFinal7],
     [vFinal8, prestacao8, amortizacao8, juro8, vFinal8],
     [vFinal9, prestacao9, amortizacao9, juro9, vFinal9],
     [vFinal10, prestacao10, amortizacao10, juro10, vFinal10],
     [vFinal11, prestacao11, amortizacao11, juro11, vFinal11],
     [vFinal12, prestacao12, amortizacao12, juro12, vFinal12]]

df = pd.DataFrame(d, columns= ["Saldo Incial", "Prestação", "Amortização", "Juros", "Saldo Final"])
print(df)