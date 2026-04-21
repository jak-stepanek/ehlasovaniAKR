import hashlib
import time
import random
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization




def inicializace_systemu():
    # Generování klíčů (soukromý pro dešifrování a PODPIS, veřejný pro šifrování a OVĚŘENÍ)
    priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pub = priv.public_key()
    return priv, pub


def zasifrovat_hlas(text_hlasu, verejny_klic):
    return verejny_klic.encrypt(
        text_hlasu.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )



def podepsat_vysledky(text_vysledku, soukromy_klic):
    # Vytvoří digitální podpis výsledné zprávy
    return soukromy_klic.sign(
        text_vysledku.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )


def overit_podpis(text_vysledku, podpis, verejny_klic):
    # Ověří, zda podpis patří autoritě a výsledky nebyly změněny
    try:
        verejny_klic.verify(
            podpis,
            text_vysledku.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except:
        return False


priv_klic, pub_klic = inicializace_systemu()
databaze_hlasu = []
stav_tokenu = {}
logy_serveru = []
finalni_vysledky_text = ""
digitalni_podpis = None


def spustit():
    global finalni_vysledky_text, digitalni_podpis
    while True:
        print("\n--- VOLEBNÍ SYSTÉM  ---")
        print("1. Registrace \n2. Hlasovat \n3. Útok \n4. Sečíst a podepsat \n5. Ověřit integritu \n6. Konec")
        volba = input("Vyberte akci: ")

        if volba == "1":
            token = f"{random.randint(1000, 9999)}"
            stav_tokenu[token] = False
            print(f">> Váš token: {token}")

        elif volba == "2":
            t = input("Token: ");
            k = input("Kandidát: ")
            if t in stav_tokenu and not stav_tokenu[t]:
                cas = time.time()
                sifra = zasifrovat_hlas(k, pub_klic)
                logy_serveru.append({"cas": cas, "token": t})
                databaze_hlasu.append({"cas": cas, "data": sifra})
                stav_tokenu[t] = True
                print(">> Hlas uložen.")
            else:
                print(">> Neplatný token.")

        elif volba == "3":
            t = input("Cílový token pro útok: ")
            cas = next((l["cas"] for l in logy_serveru if l["token"] == t), None)
            if cas:
                shoda = next((d["data"] for d in databaze_hlasu if d["cas"] == cas), None)
                print(f"!! Útok úspěšný, nalezena šifra: {shoda.hex()}")
            else:
                print(">> Token nenalezen.")

        elif volba == "4":
            vysledky = {}
            for z in databaze_hlasu:
                txt = priv_klic.decrypt(z["data"],
                                        padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(),
                                                     label=None)).decode()
                vysledky[txt] = vysledky.get(txt, 0) + 1

            finalni_vysledky_text = str(vysledky)
            # Vytvoření podpisu - sčítací autorita stvrzuje výsledky svým soukromým klíčem
            digitalni_podpis = podepsat_vysledky(finalni_vysledky_text, priv_klic)

            print(f"\n>> Hlasování uzavřeno. Výsledky: {finalni_vysledky_text}")
            print(f">> Digitální podpis vytvořen: {digitalni_podpis.hex()}")

        elif volba == "5":
            if not digitalni_podpis:
                print(">> Výsledky ještě nebyly podepsány.")
                continue

            # Simulace veřejné kontroly
            je_v_poradku = overit_podpis(finalni_vysledky_text, digitalni_podpis, pub_klic)
            if je_v_poradku:
                print("Výsledky jsou pravé.")
            else:
                print("Podpis nesouhlasí, s daty bylo manipulováno.")

        elif volba == "6":
            break


if __name__ == "__main__":
    spustit()
