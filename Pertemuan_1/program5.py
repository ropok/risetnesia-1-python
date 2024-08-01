# Perulangan print bilangan prima 1-100


# bilangan prima adalah bilangan bulat lebih dari 1 yang bukan hasilkali dari dua bilangan asli yang lebih kecil.
# kumpulkan bilangan asli lebih dari 1 dan kurang dari bilangan yang akan dicek (list)
# contoh: cek bilangan 3 : mod 1, mod 2, if hasilnya tidak ada yang 0 maka bilangan itu adalah prima

# 3

# 3 ?
# 3/2 , dst
# 3+1 = 4   range(2,4)
# 3%3 = 0

# 9 ?
# 9/2, 9/3, 9/4 dst..


# def check_prima(number):
#     if number > 1 :
#         for i in range (2, number+1):
#             if(number % i == 0):
#                 return False
#         return True
#     else:
#         return False

def check_prima(number):
    if number > 1:
        for i in range (2,number):
            if(number % i == 0):
                return False
        return True
    else:
        return False

# def check_prima(number):
#     if number > 1 :
#         for i in range (2, number):
#             if(number % i == 0):
#                 return False
#         return True
#     else:
#         return False


# for angka 1-100
for x in range(0,101):
    if(check_prima(x)):
        print(x)
