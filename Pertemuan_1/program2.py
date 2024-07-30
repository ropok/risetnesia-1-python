def reverse_word(word):
    result = ""
    # 2. akses huruf satu per satu
    word = list(word)
    max_index = len(word)-1
    # 3. baca dari belakang dan masukkan ke dalam variable result
    for x in range(max_index,-1,-1):
        result += word[x]
    return result

# 1. input kata
result = []
kata = input("Masukkan kata: ")
print("input: {}".format(kata))

# pisahkan kalimat menjadi kata
kata_terpisah = kata.split()

# tiap kata yang didapatkan, dibalik
for k in kata_terpisah:
    result.append(reverse_word(k))

# gabungkan menjadi satu kalimat kembali
result = " ".join(result)

print("output: {}".format(result))