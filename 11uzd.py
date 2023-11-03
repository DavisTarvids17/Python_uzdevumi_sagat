"""
Uzrakstiet Python programmu, lai trīskāršotu visus dotā veselo skaitļu saraksta skaitļus.
Izmantojiet Python map() funkciju.
"""

def reiztris(skaitlis):
    return skaitlis * 3

saraksts = [1, 2, 3, 4, 5]

reiztris_saraksts = list(map(reiztris, saraksts))

print("Sākotnējais saraksts:", saraksts)
print("Trīskāršotais saraksts:", reiztris_saraksts)