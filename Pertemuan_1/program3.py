# Perulangan print bilangan ganjil 1-100


# bilangan ganjil adalah bilangan yang tidak habis dibagi 2 (mod 2 != 0)
# jika bilangan tersebut ganjil, print
def check_ganjil(number):
    result = False
    if(number % 2 != 0):
        result = True
    return result

# for angka 1-100
for x in range(1,101):
    if(check_ganjil(x)):
        print(x)