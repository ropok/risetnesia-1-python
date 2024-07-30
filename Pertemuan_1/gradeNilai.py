def convert_to_grade(nilai):
    """
    100 - 90 : A
    89 - 70 : B
    69 - 50 : C
    < 50 : D
    """
    # throw error
    if(nilai <= 100 and nilai >=90):
        return "A"
    elif(nilai <= 89 and nilai >=70):
        return "B"
    elif(nilai <= 69 and nilai >=50):
        return "C"
    else:
        return "D"

input = int(input("Angka yang akan dikonvert: "))
grade_angka = convert_to_grade(input)
print("Nilai {} adalah {}".format(input,grade_angka))

str()

deklarasi
string nama = "jaler"
int angka
int number = 0
number = 0
nama = "jaler"