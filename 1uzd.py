"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

Datu struktūra - {} tā ir tukša vārdnīca, dict()
atslēga...vērtība - vārdnīca
cipari 1, 2, 3, 4, 5, 6, 7, 8, 9
"""

class AAA:
    def __init__(self):
        self.rom_cip={
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'

        }
    def uz_romu(self, num):
        result=""
        for value, sk in sorted(self.rom_cip.items(),key=lambda x:x[0], reverse=True):
            while num>=value:
                result+=sk
                num-=value

        return result
skaitlis=1984
konvertet=AAA()
rom_sks=konvertet.uz_romu(skaitlis)
print(f"{skaitlis} romiešu ciparos ir {rom_sks}.")