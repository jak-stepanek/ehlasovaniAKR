import hashlib
import os
import time


def sha256_trunc_bits(m, t):
    h = hashlib.sha256(m).digest()
    h_int = int.from_bytes(h, "big")
    return h_int >> (256 - t)


def birthday_attack(t):
    seen = {}
    pokusy = 0
    start = time.time() #cas k odecteni

    while True:
        m = os.urandom(12)
        h = sha256_trunc_bits(m, t) #zkraceny hash
        pokusy += 1

        if h in seen and seen[h] != m:  #m1!=m2, trunc(m1)==trunc(m2)
            doba_trvani = time.time() - start #vypocet casu
            m1=seen[h]
            m2=m
            return pokusy, doba_trvani, m1, m2, h

        seen[h] = m #ulozeni do slovniku


tests = [8, 16, 20, 24, 28, 32]


for t in tests:
    pokusy, doba_trvani, m1, m2, h = birthday_attack(t)
    teorie = 1.1774 * 2**(t/2)

    print(f"\nt = {t}")
    print(f"realne pokusy: {pokusy}|teoreticke pokusy: {int(teorie)}")
    print(f"cas:{round(doba_trvani,4)} s |hash: {h}" )
    print(f"m1: {m1.hex()}|m2:{m2.hex()}")
