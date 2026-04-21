import math

a = "1111101101011110011111101100010111001010101111110111111011111011001100001001111110111101110110111101011001111101001101101010101111111101011110101110111110111111111111100011111101101111110111111110101010100101111110011101111110110101010000110101011110110100000110101001010111100110101111110111100111111111001111111110011011111111101110110101110000100111110111111001111011101101111111010111010111010111111111111111111111111011101100101110011011111000101111111111011110111110011000011011011010111110111111010101011101111010111111011001111110001111111001101001001110010111000110110111010011111111100011011111111001111101110111011010110100111111111111011110011001110011111111110111011100000100011110011001111111011111110001101111101111111111001111011111010110010011101110110101111110101110111010111011011100011011011101110010001100111111111111001011000001010101011001111011111110011111111011110001101011101011011111111011010111001100101001101110111111101111111001111111111111011100110111111111111101101110"
b = "0111010000110010101101000000010001011100100111110011100110110101111010101100000000101110100110100110110010001111100011101001001001001100110110010011001110000100111111000111100110110100110111110001010101000110001010100101100101100011000000010111111110110001010111111101111111011010110100000010100111001010010010010110110011110010110100010100000010011000110101101010100110010000011111010101000010100000101010011100110101011101101000010111001001001110100000100110011010000111010010001001110101111101100111100011010110010101111001111011111100001110101001111111001100101100111110111011111111111000100101011000011000000011000010011010101001011010011100011110011110101111011111111111000000110111110001000110010011111001000001101111101101110000001110100010101011111011110100111011111100010010110000001010000111010111110011111100101101111100111001001110111001110011110000110000000100000100100110011101111100111111001111111000011101111111011111110001011101100111011111001110111011101000110111111111100101011110"

n0a = a.count("0")
n0b = b.count("0")

n1a = a.count("1")
n1b = b.count("1")

pocet_bitu_a = n0a + n1a
pocet_bitu_b = n0b + n1b
print("----Pravděpodobnosti------")
print(f"V řetězci a je {n0a} 0 a {n1a} 1 a celkovy pocet bitu je {pocet_bitu_a}")
print(f"V řetězci b je {n0b} 0 a {n1b} 1 a celkovy pocet bitu je {pocet_bitu_b}\n")

pravdepodobnost_1a = n1a / pocet_bitu_a
pravdepodobnost_0a = n0a / pocet_bitu_a

pravdepodobnost_1b = n1b / pocet_bitu_b
pravdepodobnost_0b = n0b / pocet_bitu_b

print(f"Pravděpodobnost 1 v řetězci a je {pravdepodobnost_1a} a pravděpodobnost 0 = {pravdepodobnost_0a}, tato posloupnost je nevyvážená protože převažují 1")
print(f"Pravděpodobnost 1 v řetězci b je {pravdepodobnost_1b} a pravděpodobnost 0 = {pravdepodobnost_0b}, tato posloupnost je vyvážená, protože má podobně 1 a 0\n")

print("----Shannonova Entropie a Min Entropie -----")
shaE_a = (-pravdepodobnost_0a) * math.log2(pravdepodobnost_0a) - pravdepodobnost_1a * math.log2(pravdepodobnost_1a)
if(pravdepodobnost_1a > pravdepodobnost_0a):
    minE_a = -math.log2(pravdepodobnost_1a)
else:
    minE_a = -math.log2(pravdepodobnost_0a)
print(f"Posloupnost a: Shannonova entropie = {shaE_a}, Min-entropie = {minE_a}")

shaE_b = (-pravdepodobnost_0b) * math.log2(pravdepodobnost_0b) - pravdepodobnost_1b * math.log2(pravdepodobnost_1b)
if(pravdepodobnost_1b > pravdepodobnost_0b):
    minE_b = -math.log2(pravdepodobnost_1b)
else:
    minE_b = -math.log2(pravdepodobnost_0a)

print(f"Posloupnost b: Shannonova entropie = {shaE_b}, Min-entropie = {minE_b}\n\n")

# Shannonova entropie udává průměrnou míru neurčitosti
# Min-entripoe udává nejpravděpodobnější výsledek (nejhorší scénář) z hlediska předvídatelnosti

#Monobit test

S_a = n1a - n0a
S_b = n1b - n0b

Sobs_a = abs(S_a) / math.sqrt(pocet_bitu_a)
Sobs_b = abs(S_b) / math.sqrt(pocet_bitu_b)
print("-----Monobit test----")
print(f"{Sobs_a} = nepřijatelná hodnota")
print(f"{Sobs_b} = přijatelná hodnota\n\n")
# Hodnota 2,58 zde představuje hranici, podle které posuzujeme, zda se chování posloupnosti ještě dá považovat za běžné, nebo už příliš vybočuje.
# Pokud je S_obs menší nebo rovno této hodnotě, posloupnost je považována za náhodnou.
# Pokud je  S_obs větší, posloupnost se od očekávaného chování odchyluje natolik, že ji označíme za podezřelou.

print("-----Von neunannova metoda A-----")
nova_posloupnost_a = ""
pocet_00 = 0
pocet_01 = 0
pocet_10 = 0
pocet_11 = 0

for i in range(0, len(a) -1, 2):
    dvojice = a[i:i+2]

    if dvojice == "00":
        pocet_00 += 1
    elif dvojice == "01":
        pocet_01 += 1
        nova_posloupnost_a += "0"
    elif dvojice == "10":
        pocet_10 += 1
        nova_posloupnost_a += "1"
    elif dvojice == "11":
        pocet_11 += 1


nova_delka_a = len(nova_posloupnost_a)
pocet_nula = nova_posloupnost_a.count("0")
pocet_jednaa = nova_posloupnost_a.count("1")
p1a = pocet_jednaa/nova_delka_a
p0a = pocet_nula/nova_delka_a
shaa =(-p0a)*math.log2(p0a) - (p1a)*math.log2(p1a)
mina = -math.log2(max(p0a, p1a))

print("Počet dvojic 00:", pocet_00)
print("Počet dvojic 01:", pocet_01)
print("Počet dvojic 10:", pocet_10)
print("Počet dvojic 11:", pocet_11)


print("\nNová posloupnost a:", nova_posloupnost_a)
print("Nová délka posloupnosti:", nova_delka_a)
print("Počet nul po korekci:", pocet_nula)
print("Počet jedniček po korekci:", pocet_jednaa)
print("Odhad P^(0):", p0a)
print("Odhad P^(1):", p1a)
print("Shannonova entropie po korekci:", shaa)
print("Min-entropie po korekci:", mina)


print("\n\n-----Von neunannova metoda B-----")
nova_posloupnost_b = ""
pocet_00b = 0
pocet_01b = 0
pocet_10b = 0
pocet_11b = 0

for i in range(0, len(b) -1, 2):
    dvojiceb = b[i:i+2]

    if dvojiceb == "00":
        pocet_00b += 1
    elif dvojiceb == "01":
        pocet_01b += 1
        nova_posloupnost_b += "0"
    elif dvojiceb == "10":
        pocet_10b += 1
        nova_posloupnost_b += "1"
    elif dvojiceb == "11":
        pocet_11b += 1


nova_delka_b = len(nova_posloupnost_b)
pocet_nulb = nova_posloupnost_b.count("0")
pocet_jednab= nova_posloupnost_b.count("1")
p1b = pocet_jednab/nova_delka_b
p0b = pocet_nulb/nova_delka_b
shab =(-p0b)*math.log2(p0b) - (p1b)*math.log2(p1b)
minb = -math.log2(max(p0b, p1b))

print("Počet dvojic 00:", pocet_00b)
print("Počet dvojic 01:", pocet_01b)
print("Počet dvojic 10:", pocet_10b)
print("Počet dvojic 11:", pocet_11b)


print("\nNová posloupnost b:", nova_posloupnost_b)
print("Nová délka posloupnosti:", nova_delka_b)
print("Počet nul po korekci:", pocet_nulb)
print("Počet jedniček po korekci:", pocet_jednab)
print("Odhad P^(0):", p0b)
print("Odhad P^(1):", p1b)
print("Shannonova entropie po korekci:", shab)
print("Min-entropie po korekci:", minb)

"""
Otázky:
1. Byla původní posloupnost vyvážená?
posloupnost a na začátku vyvážená nebyla protže zde byla výrazná převaha jedniček
posloupnost b byla vyvážená už od začátku

2.Co ukázala Shannonova entropie a min-entropie?
Shannonova entropie vyjádřila průměrnou míru neurčitosti v posloupnosti, tedy jak vyváženě a rozmanitě se v ní bity objevují jako celek. Min-entropie zachytila nejméně příznivý případ.
U posloupnosti A byl mezi Shannonovou entropií a min-entropií výraznější rozdíl.I když posloupnost stále obsahovala určitou míru neurčitosti v průměru, zároveň v ní byl jeden symbol, konkrétně jednička, zastoupen častěji. Posloupnost tedy nebyla dobře vyvážená a slabší
U posloupnosti b vyšly obě entropie poměrně vysoké. To ukazuje, že rozdělení nul a jedniček bylo vyrovnanější a žádný symbol v ní nepřevažoval tak výrazně.

3. Zlepšila von Neumannova metoda vyváženost výstupu?
Ano u obou posloupností

4.Jaký byl dopad korekce na délku posloupnosti?
Dopad na délku posloupnosti byl výrazný na A i B. Posloupnost a se z n=1000 zkrátila na n=218  a posloupnost B se zkrátila z n=1000 na n= 236.

5. Proč ani po těchto výpočtech nelze automaticky tvrdit, že zdroj je kryptograficky bezpečný?
vyváženost nul a jedniček sama nestačí, vysoká entropie neznamená automaticky nepředvídatelnost, zdroj může mít závislosti mezi bity, mohou existovat vzory,




"""





