# 1. input kata
kata = input("Masukkan kata: ")
print(kata)

# 2. baca huruf satu per satu
kata_terpisah = list(kata)

# 3. dari list kata_terpisah dibalik, baca dari belakang
kata_terbalik = ""

panjang_words = len(kata_terpisah) -1

for x in range(panjang_words,-1,-1):
    y = kata_terpisah[x]
    kata_terbalik += y

print(kata_terbalik)