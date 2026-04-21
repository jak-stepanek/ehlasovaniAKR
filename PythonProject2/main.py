import hashlib
import random
import secrets
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# --- JÁDRO SYSTÉMU ---

def inicializace_systemu():
    priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pub = priv.public_key()
    return priv, pub


def zasifrovat_hlas(text_hlasu, verejny_klic):
    return verejny_klic.encrypt(
        text_hlasu.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )


def vypocitat_hash_db(db):
    # Pro kontrolu integrity zahashujeme celou databázi jako řetězec
    return hashlib.sha256(str(db).encode()).hexdigest()


# --- PROMĚNNÉ SYSTÉMU ---
priv_klic, pub_klic = inicializace_systemu()
databaze_hlasu = []  # List of dicts: {"data": encrypted_bytes}
stav_tokenu = {}  # Token: Použit (True/False)
referencni_hash = ""  # Hash uložený v okamžiku uzavření voleb


def spustit():
    global referencni_hash
    while True:
        print("\n--- volební systém ---")
        print(
            "1. Registrace \n2. Hlasovat \n3. Uzavřít a uložit hash \n4. útok \n5. Ověřit integritu \n6. Konec")
        volba = input("Vyberte akci: ")

        if volba == "1":
            token = secrets.token_hex(3)
            stav_tokenu[token] = False
            print(f">> Váš token: {token}")

        elif volba == "2":
            t = input("Token: ")
            k = input("Kandidát: ")
            if t in stav_tokenu and not stav_tokenu[t]:
                sifra = zasifrovat_hlas(k, pub_klic)
                databaze_hlasu.append({"data": sifra})
                stav_tokenu[t] = True
                print(">> Hlas úspěšně uložen do databáze.")
            else:
                print(">> CHYBA: Neplatný token.")

        elif volba == "3":
            referencni_hash = vypocitat_hash_db(databaze_hlasu)
            print(f">> Volby uzavřeny. Referenční hash integrity: {referencni_hash}")

        elif volba == "4":
            if not databaze_hlasu:
                print(">> Databáze je prázdná, není co měnit.")
                continue
            # SIMULACE MANIPULACE: Změníme jeden náhodný hlas
            index = random.randint(0, len(databaze_hlasu) - 1)
            puvodni_data = bytearray(databaze_hlasu[index]["data"])
            puvodni_data[0] ^= 0xFF  # Změna prvního bajtu (bitový flip)
            databaze_hlasu[index]["data"] = bytes(puvodni_data)
            print(f"!! MANIPULACE: Data v záznamu č. {index + 1} byla tajně změněna útočníkem.")

        elif volba == "5":
            if not referencni_hash:
                print(">> Nejdříve uzavřete volby , aby se vytvořil hash k porovnání.")
                continue

            aktualni_hash = vypocitat_hash_db(databaze_hlasu)
            print(f"Referenční hash: {referencni_hash}")
            print(f"Aktuální hash:   {aktualni_hash}")

            if aktualni_hash == referencni_hash:
                print("Žádná data nebyla změněna.")
            else:
                print("Hash se neshoduje, s databází bylo manipulováno.")

        elif volba == "6":
            break


if __name__ == "__main__":
    spustit()