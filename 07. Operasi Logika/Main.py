""" 
Operasi logika atau boolean

ada beberapa jenis operasi logika boolean 
    and     =   &&  operasi ke dua syaray harus di penuhi akan true
    or      =   ||  operasi jika salah satu syarat termenuhi maka true
    xor     =   ^   operasi jika salah satu benar jadi tidak boleh benar ke dua nya
    not     =   !   operasi negasi atau kebalikan
"""

Benar = True
Salah = False

# not 
print("===NOT")
Hasil = not Salah
print(Benar,"NOT",Salah," : ", Hasil)

# AND
print("\n===AND")
Hasil = Benar and Benar
print(Benar,"and",Benar," : ", Hasil)
Hasil = Benar and Salah
print(Benar,"and",Salah," : ", Hasil)
Hasil = Salah and Benar
print(Salah,"and",Benar," : ", Hasil)
Hasil = Salah and Salah
print(Salah,"AND",Salah," : ", Hasil)

# OR
print("\n===OR")
Hasil = Benar or Benar
print(Benar,"OR",Benar," : ", Hasil)
Hasil = Benar or Salah
print(Benar,"OR",Salah," : ", Hasil)
Hasil = Salah or Benar
print(Salah,"OR",Benar," : ", Hasil)
Hasil = Salah or Salah
print(Salah,"OR",Salah," : ", Hasil)

# xOR
print("\n===XOR")
Hasil = Benar ^ Benar
print(Benar,"XOR",Benar," : ", Hasil)
Hasil = Benar ^ Salah
print(Benar,"XOR",Salah," : ", Hasil)
Hasil = Salah ^ Benar
print(Salah,"XOR",Benar," : ", Hasil)
Hasil = Salah ^ Salah
print(Salah,"XOR",Salah," : ", Hasil)