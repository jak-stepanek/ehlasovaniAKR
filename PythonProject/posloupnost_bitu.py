import math
data1="1111101101011110011111101100010111001010101111110111111011111011001100001001111110111101110110111101011001111101001101101010101111111101011110101110111110111111111111100011111101101111110111111110101010100101111110011101111110110101010000110101011110110100000110101001010111100110101111110111100111111111001111111110011011111111101110110101110000100111110111111001111011101101111111010111010111010111111111111111111111111011101100101110011011111000101111111111011110111110011000011011011010111110111111010101011101111010111111011001111110001111111001101001001110010111000110110111010011111111100011011111111001111101110111011010110100111111111111011110011001110011111111110111011100000100011110011001111111011111110001101111101111111111001111011111010110010011101110110101111110101110111010111011011100011011011101110010001100111111111111001011000001010101011001111011111110011111111011110001101011101011011111111011010111001100101001101110111111101111111001111111111111011100110111111111111101101110"
data2="0111010000110010101101000000010001011100100111110011100110110101111010101100000000101110100110100110110010001111100011101001001001001100110110010011001110000100111111000111100110110100110111110001010101000110001010100101100101100011000000010111111110110001010111111101111111011010110100000010100111001010010010010110110011110010110100010100000010011000110101101010100110010000011111010101000010100000101010011100110101011101101000010111001001001110100000100110011010000111010010001001110101111101100111100011010110010101111001111011111100001110101001111111001100101100111110111011111111111000100101011000011000000011000010011010101001011010011100011110011110101111011111111111000000110111110001000110010011111001000001101111101101110000001110100010101011111011110100111011111100010010110000001010000111010111110011111100101101111100111001001110111001110011110000110000000100000100100110011101111100111111001111111000011101111111011111110001011101100111011111001110111011101000110111111111100101011110"
pocet_nul_A = data1.count("0")
pocet_nul_B = data2.count("0")


pocet_jednicek_A = data1.count("1")
pocet_jednicek_B = data2.count("1")


celkovy_pocet_A = len(data1)
celkovy_pocet_B = len(data2)


p0_A = (pocet_nul_A / celkovy_pocet_A)
p0_B = (pocet_nul_B / celkovy_pocet_B)


p1_A = 1-p0_A
p1_B = 1-p0_B



ShEntropie_A = -p0_A * math.log(p0_A,2)-p1_A * math.log(p1_A,2)
ShEntropie_B = -p0_B * math.log(p0_B,2)-p1_B * math.log(p1_B,2)

MinEntropie_A = -math.log(max(p0_A,p1_A),2)
MinEntropie_B = -math.log(max(p0_B,p1_B),2)


p_A = pocet_jednicek_A-pocet_nul_A
p_B = pocet_jednicek_B-pocet_nul_B

sobs_A = (abs(p_A))/math.sqrt(celkovy_pocet_A)
sobs_B = (abs(p_B))/math.sqrt(celkovy_pocet_B)


posloupnost_A2 = ""
pocet00_A = 0
pocet01_A = 0
pocet10_A = 0
pocet11_A = 0

for i in range(0, len(data1)-1,2):
    dvojice = data1[i:i+2]
    if dvojice == "00":
        pocet00_A += 1
    elif dvojice == "01":
        pocet01_A += 1
        posloupnost_A2 += "0"
    elif dvojice == "10":
        pocet10_A += 1
        posloupnost_A2 += "1"
    elif dvojice == "11":
        pocet11_A += 1

delka_A2 = len(posloupnost_A2)
pocet_nul_A2 = posloupnost_A2.count("0")
pocet_jednicek_A2 = posloupnost_A2.count("1")
p0_A2 = (pocet_nul_A2 / delka_A2)
p1_A2 = 1-p0_A2
ShEntropie_A2 = -p0_A2 * math.log(p0_A2,2)-p1_A2 * math.log(p1_A2,2)
MinEntropie_A2 = -math.log(max(p0_A2,p1_A2),2)




posloupnost_B2 = ""
pocet00_B = 0
pocet01_B = 0
pocet10_B = 0
pocet11_B = 0

for i in range(0, len(data2)-1,2):
    dvojice = data2[i:i+2]
    if dvojice == "00":
        pocet00_B += 1
    elif dvojice == "01":
        pocet01_B += 1
        posloupnost_B2 += "0"
    elif dvojice == "10":
        pocet10_B += 1
        posloupnost_B2 += "1"
    elif dvojice == "11":
        pocet11_B += 1
delka_B2 = len(posloupnost_B2)
pocet_nul_B2 = posloupnost_B2.count("0")
pocet_jednicek_B2 = posloupnost_B2.count("1")
p0_B2 = (pocet_nul_B2 / delka_B2)
p1_B2 = 1-p0_B2
ShEntropie_B2 = -p0_B2 * math.log(p0_B2,2)-p1_B2 * math.log(p1_B2,2)
MinEntropie_B2 = -math.log(max(p0_B2,p1_B2),2)

print("#########################################")
print("POSLOUPNOST 1:\n")
print(f"v posloupnosti je {pocet_nul_A} nul")
print(f"v posloupnosti je {pocet_jednicek_A} jednicek")
print(f"v posloupnosti je {celkovy_pocet_A} bitu\n")
print (f"pravdepodobnost nuly je {p0_A * 100}%, pravdepodobnost jednicky je {p1_A * 100}%")
if p0_A < 0.5:
    print("posloupnost neni vyvazena - bias je na strane jednicek\n")
elif p0_A > 0.5:
    print("posloupnost neni vyvazena, bias je na strane nul\n")
else:
    print("posloupnost je vyvazena\n")
print(f"Shannonova Entropie: {ShEntropie_A}")
print(f"Min-Entropie: {MinEntropie_A}\n")
# shannonova entropie popisuje průměrnou míru neurčitosti, min-entropie ukazuje minimální. Pro kryptografii je důležitější hodnota min-entropie, z důvodu nejjednodušší možnosti pro uhádnutí posloupnosti.
print(f"výsledek monobit testu:{sobs_A}")
if sobs_A <= 2.58:
    print("posloupnost je vhodná podle monobit testu")
else:
    print("posloupnost je příliš podezřelá podle monobit testu\n")
print("#############################")
print("Von Neumannova metoda posloupnosti A:\n")
print(f"v posloupnosti je {pocet_nul_A2} nul")
print(f"v posloupnosti je {pocet_jednicek_A2} jednicek")
print(f"v posloupnosti je {delka_A2} bitu\n")
print (f"pravdepodobnost nuly je {p0_A2 * 100}%, pravdepodobnost jednicky je {p1_A2 * 100}%")
if p0_A2 < 0.5:
    print("posloupnost neni vyvazena - bias je na strane jednicek\n")
elif p0_A2 > 0.5:
    print("posloupnost neni vyvazena, bias je na strane nul\n")
else:
    print("posloupnost je vyvazena\n")
print(f"Shannonova Entropie: {ShEntropie_A2}")
print(f"Min-Entropie: {MinEntropie_A2}\n\n")
print("##############################")
print("##############################")
print("##############################")
print("##############################")
print("#########################################")
print("POSLOUPNOST 2:\n")
print(f"v posloupnosti je {pocet_nul_B} nul")
print(f"v posloupnosti je {pocet_jednicek_B} jednicek")
print(f"v posloupnosti je {celkovy_pocet_B} bitu\n")
print (f"pravdepodobnost nuly je {p0_B * 100}%, pravdepodobnost jednicky je {p1_B * 100}%")
if (p0_B < 0.5):
    print("posloupnost neni vyvazena - bias je na strane jednicek\n")
elif p0_B > 0.5:
    print("posloupnost neni vyvazena, bias je na strane nul\n")
else:
    print("posloupnost je vyvazena\n")
print(f"Shannonova Entropie: {ShEntropie_B}")
print(f"Min-Entropie: {MinEntropie_B}\n")
# shannonova entropie popisuje průměrnou míru neurčitosti, min-entropie ukazuje minimální. Pro kryptografii je důležitější hodnota min-entropie, z důvodu nejjednodušší možnosti pro uhádnutí posloupnosti.
print(f"výsledek monobit testu:{sobs_B}")
if sobs_B <= 2.58:
    print("posloupnost je vhodná podle monobit testu")
else:
    print("posloupnost je příliš podezřelá podle monobit testu\n")
print("#############################")
print("Von Neumannova metoda posloupnosti B:\n")
print(f"v posloupnosti je {pocet_nul_B2} nul")
print(f"v posloupnosti je {pocet_jednicek_B2} jednicek")
print(f"v posloupnosti je {delka_B2} bitu\n")
print (f"pravdepodobnost nuly je {p0_B2 * 100}%, pravdepodobnost jednicky je {p1_B2 * 100}%")
if p0_B2 < 0.5:
    print("posloupnost neni vyvazena - bias je na strane jednicek\n")
elif p0_B2 > 0.5:
    print("posloupnost neni vyvazena, bias je na strane nul\n")
else:
    print("posloupnost je vyvazena\n")
print(f"Shannonova Entropie: {ShEntropie_B2}")
print(f"Min-Entropie: {MinEntropie_B2}\n\n")
print("######################")
"""
 shannonova entropie popisuje průměrnou míru neurčitosti, min-entropie ukazuje minimální. Pro kryptografii je důležitější hodnota min-entropie, z důvodu nejjednodušší možnosti pro uhádnutí posloupnosti.

Otázky:
1) Byla původní posloupnost vyvážená?
    Ani jedna z posloupností nebyla dokonale vyvážená, ale posloupnost B se vyváženosti blížila

2) Co ukázala Shannonova entropie a min-entropie?
    Čím větší rozdíl je mezi shannonovou entropií a min-entropií, tím méně je posloupnost vhodná ke kryptografickým účelům
     Posloupnost B byla vhodnější, ale po von neumannove metodě měla posloupnost z posl. A menší rozdíl

3) Zlepšila von Neumannova metoda vyváženost výstupu?
    Ano, podstatně

4) Jaký byl dopad korekce na délku posloupnosti?
    Obě posloupnosti byly zkráceny na přibližnou devítinu jejich původní délky

5) Proč ani po těchto výpočtech nelze automaticky tvrdit, že zdroj je kryptograficky bezpečný?
    Mezi bity se mohou objevovat vzory nebo se opakovat, tuto problematiku tímto řešením nijak neošetřujeme

"""