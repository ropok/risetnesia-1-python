"""
binary
0 1 01 001
0: 00
1: 01
2: 10
3: 11

3 =>
    ambil 2**n <= 3:
        catat nilai n
        masukkan digit 1 ke dalam list[n]
    temp_nilai: 2**n - 3 = 0?
        iya: dicatat nilai n sampai ke 0: adalah 0
        tidak: cari 2**n yang nilainya <= temp_nilai

"""

def to_binary(number):
    n = 0
    temp_nilai = 0
    list_binary = [0,0]
    for i in range (0,len(list_binary)):
        temp_nilai = 2**i
        if(temp_nilai >= number):

        # temp_nilai = 2**i - number


"""
input: 3
1. 2**0 = 1
2. 2**1 = 2
3. 2**2 = 4, hasilnya >=3, berarti kita dapat digit terjauh; n-1
    catat hasil sisa: 3-2 = 1
4. Keluar dari for (break)
5. list[n-1] = 1
    list[1] = 1
6. cari list[0]
7. 2**0 = 1, hasilnya >=1
    menemukan nilai list[0]: 1
8. list[] = 1,1
9. hasil sisa 1-1 = 0
10. jika hasil sisa = 0, selesai
11. menerjemahkan list yang udah dapat ke format binary
"""

"""
binary ke desimal

1101
list(1101) => 1 1 0 1
len list 
reversed => 1 0 1 1
2**i
catat indexnya 
result += 2**i
print result


"""