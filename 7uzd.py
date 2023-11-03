"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""


saraksts1 = ["Kalniņš", "Opmanis", "Vēzis", "Almane"]
saraksts2 = []

for uzvards in saraksts1:
    doktors = "Dr. " + uzvards
    saraksts2.append(doktors)

print(saraksts2)

