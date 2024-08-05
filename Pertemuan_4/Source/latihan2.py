"""
2. Permainan kartu. Kartu remi, kita batasi AS King Queen Jack 10. Ada 2 orang bermain kartu tersebut, setiap round masing-masing orang menentukan mau keluarkan kartu yang mana, tentukan mana yang menang berdasarkan kartu yang muncul. Contoh Jack vs Queen, menang Queen. Kartu 10 dengan kartu 10 hasilnya Seri.
"""

"""
1. kartu remi
    AS King Queen Jack 10
    tuple1 = ("10", "Jack", "Queen", "King", "AS")
2. orang1 "Jack" vs orang2 "AS"
    ambil index: compare, hasil akhirnya orang1 pemenangnya.
    hasil sama: 
3. Class: orang (def: mengeluarkan kartu ("AS"))
4. orang1, orang2
"""

tuple1 = ("10", "Jack", "Queen", "King", "AS")

result = tuple1.index("Queen")
print(result)

def keluar_kartu(deck,kartu):
    return deck.index(kartu)

def bandingkan_kartu(kartu1,kartu2):
    if(kartu1 > kartu2):
        return "pemain 1 menang"
    elif(kartu1 < kartu2):
        return "pemain 2 menang"
    else:
        return "SERI"