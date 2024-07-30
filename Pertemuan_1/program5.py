# Perulangan print bilangan prima 1-100


# bilangan prima adalah bilangan bulat lebih dari 1 yang bukan hasilkali dari dua bilangan asli yang lebih kecil.
# kumpulkan bilangan asli lebih dari 1 dan kurang dari bilangan yang akan dicek (list)
# contoh: cek bilangan 3 : mod 1, mod 2, if hasilnya tidak ada yang 0 maka bilangan itu adalah prima

# 3

def check_prima(number):
    if number > 1:
        for x in range (2,number+1):
            if(number % x == 0):
                return False
            else:
                return True
    else:
        return False




# for angka 1-100
for x in range(0,10):
    if(check_prima(x)):
        print(x)
