"""
Uzdevumā izmantot funkciju map(), kura  komandu izpilda 
katram saraksta(virknes) loceklim.

"""

def izpilde(loceklis):
    return "Izpildīta komanda: " + loceklis

saraksts = ["komanda1", "komanda2", "komanda3"]

rezultats = list(map(izpilde, saraksts))

for rezultats_loceklis in rezultats:
    print(rezultats_loceklis)