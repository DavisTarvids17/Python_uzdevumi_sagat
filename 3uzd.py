"""
Uzrakstiet programmu, izveidot klasi ar nosaukumu
Dati. Izveidot objektu, kas inicializētu atribūtus, 
piemēram, vārdu, vecumu un ceļojumam iemaksāto summu.

"""
class Dati:
    def __init__(self, vards, vecums, iemaksa_celojumam):
        self.vards = vards
        self.vecums = vecums
        self.iemaksa_celojumam = iemaksa_celojumam

# Izveidojam objektu ar norādītajiem atribūtiem
mans_objekts = Dati("Doms", 29, 350)


