# Tahun kabisat: 2020 -> ini adalah tahun kabisat

# tahun kabisat adalah yang habis dibagi 4 (4 tahun sekali)
def is_kabisat(year):
    if(year % 4 == 0):
        return True
    else:
        return False

input_tahun = input("Check tahun kabisat: ")
if(is_kabisat(int(input_tahun))):
    print("{} adalah tahun kabisat".format(input_tahun))
else:
    print("{} bukan merupakan tahun kabisat".format(input_tahun)) 