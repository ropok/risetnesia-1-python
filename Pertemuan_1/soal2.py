def reverse_word(word):
    result = ""
    # 2. akses huruf satu per satu
    word = list(word)
    max_index = len(word)-1
    # 3. baca dari belakang dan masukkan ke dalam variable result
    for x in range(max_index,-1,-1):
        result += word[x]
    return result

# input kata
input_kata = input("masukan kata / kalimat yang dibalik: ")
# pisahkan kata / kalimat
list_kata = input_kata.split()
print(list_kata)

# list kata kita balik
temp_kata = ""
list_hasil_kata = []
for kata in list_kata:
    temp_kata = reverse_word(kata)
    list_hasil_kata.append(temp_kata)

hasil_akhir = " ".join(list_hasil_kata)
print(hasil_akhir)