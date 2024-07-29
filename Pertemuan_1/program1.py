def main():
    print("Hello World")


# 1. input kata
kata = input("Masukkan kata: ")
print(kata)

# 2. baca huruf satu per satu
# kata_terpisah = kata.split() # hasilnya berupa list: ['kata'] memisahkan kalimat
# print(kata_terpisah)
# panjang_kata = len(kata_terpisah)
# print(panjang_kata)
kata_terpisah = list(kata)
# print(kata_terpisah)
# print(len(kata_terpisah))

# 3. dari list kata_terpisah dibalik, baca dari belakang
kata_terbalik = ""

panjang_words = len(kata_terpisah) -1

for x in range(panjang_words,-1,-1):
    y = kata_terpisah[x]
    kata_terbalik += y

print(kata_terbalik)