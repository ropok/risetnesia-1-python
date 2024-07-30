# tahun kabisat
# kabisat = 4 tahun sekali
# habis dibagi 4 (% 4)

def is_kabisat(tahun):
    if(tahun % 4 == 0):
        return True
    else:
        return False

def check_ganjil(number):
    if number % 2 != 0:
        return True # iya ini ganjil
    else:
        return False # ini bukan ganjil

number = int(input("masukan angka: "))
if(check_ganjil(number)):
    print("{} adalah ganjil".format(number))
else:
    print("ini genap")

tahun = int(input("Check tahun kabisat: "))
bool_is_kabisat = is_kabisat(tahun)
if(bool_is_kabisat):
    print("{} adalah tahun kabisat".format(tahun))
else:
    print("{} ini bukan tahun kabisat".format(tahun))