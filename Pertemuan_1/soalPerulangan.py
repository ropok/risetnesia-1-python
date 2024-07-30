# print bilangan ganjil 1 - 100

# bilangan dianggap ganjil
# bilangan ganjil = tidak dihabis 2 (mod %)
def check_ganjil(number):
    if number % 2 != 0:
        return True # iya ini ganjil
    else:
        return False # ini bukan ganjil

def check_genap(number):
    if number % 2 == 0:
        return True # iya ini ganjil
    else:
        return False # ini bukan ganjil

# prima: bilangan asli > 1, hanya habis dibagi bilangan asli yang lebih kecil
def check_prima(number):
    if number > 1:
        for x in range(2, number+1):
            if (number % x == 0):
                return False
            else:
                return True
    else:
        return False

# check di angka 1 - 100

# program utama
for i in range (1,20):
    if(check_prima(i)):
        print(i)
