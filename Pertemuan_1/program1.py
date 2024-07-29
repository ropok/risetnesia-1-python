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
kata = input("Masukkan kata: ")
print("input: {}".format(kata))

kata_terbalik = reverse_word(kata)
print("output: {}".format(kata_terbalik))