""" 
Operasi aritmatika

pada python untuk operasi tambah,kali,bagi,kurang,modulus simbolnya sama
    +   =   tambah
    *   =   kali
    /   =   bagi
    -   =   kurang
    %   =   sisa bagi (modulus)

ada beberapa operator tambahan pada python
    **  =   operator eskonensial atau pangkat
    //  =   operator floor division atau pembagian yang nilainya di ambil nilai terkecil

prioritas pengerjaan dalam simbol
    1. () di utamakan
    2. eksponensial ** 
    3. perkalian dan teman"nya  * / % //
 """

a = 5
b = 3

# Tambah +
hasil = a + b
print(a,"+",b,"=",hasil)

# Kali *
hasil = a * b
print(a,"*",b,"=",hasil)

# Kurang -
hasil = a - b
print(a,"-",b,"=",hasil)

# Bagi /
hasil = a / b
print(a,"/",b,"=",hasil)

# Modulus
hasil = a % b
print(a,"%",b,"=",hasil)

# Eskponen **
hasil = a ** b
print(a,"**",b,"=",hasil)

# Floor division
hasil = a // b
print(a,"//",b,"=",hasil)