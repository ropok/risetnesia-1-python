"""
1. Sistem pencatatan score basket, tampilkan score home dan visitor. Nilai score berdasarkan aturan basket pada umumnya.
Output yang dihasilkan berupa cetakan goal dengan detail berapa poin yang dihasilkan, jenis goalnya, tim mana yang mencetak goal dan hasil score saat itu (home vs visitor).
"""

"""
Output:
1. jenis cetakan poin: 1poin(1), 2poin(2), 3poin(3)
    dictionary: {"1p" : 1, "2p" : 2, "3p" : 3}
2. Tim yang mencetak goal (home atau visitor) contoh: "Home mencetak goal"
    input: tim yang mencetak, jenis cetakan poin. Output poin yang dihasilkan oleh Home(int)
3. Display hasil akhir score: Home: ... poin, Visitor: ... poin
    input: score home berapa, score visitor berapa
"""

dict1 = {"1p" : 1, "2p" : 2, "3p" : 3}
def cetak_goal(tim,dict1,jenis_poin):
    print(tim + " mencetak poin")
    poin = dict1[jenis_poin]
    return poin

def display_score(poin_home,poin_visitor):
    print("Home: {}, Visitor: {}".format(poin_home,poin_visitor))

