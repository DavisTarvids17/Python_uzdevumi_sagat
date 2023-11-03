"""
Uzrakstiet Python programmu, lai diviem sarakstiem noteikti atšķirību.
Izmantojiet funkciju map().
"""
# variants 1
# Sākotnējie saraksti
saraksts1 = [1, 2, 3, 4, 5]
saraksts2 = [3, 4, 5, 6, 7]
 
# Funkcija, kas aprēķina atšķirību starp diviem skaitļiem
def atslega(skaitlis1, skaitlis2):
    return skaitlis1 - skaitlis2
 
# Izmantot map() funkciju, lai iegūtu atšķirības starp sarakstiem
atshiribas_saraksts = list(map(atslega, saraksts1, saraksts2))
 
print(atshiribas_saraksts)

# variants 2

# Sākotnējie saraksti
saraksts1 = [1, 2, 3, 4, 5]
saraksts2 = [3, 4, 5, 6, 7]
 
# Izveidojam jaunu tukšu sarakstu atšķirībām
atshiribas_saraksts = []
 
# Aprēķinam atšķirības starp sarakstiem, izmantojot for ciklu
for skaitlis1, skaitlis2 in zip(saraksts1, saraksts2):
    atshiriba = skaitlis1 - skaitlis2
    atshiribas_saraksts.append(atshiriba)
 
print(atshiribas_saraksts)