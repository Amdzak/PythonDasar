""" 
TIPE DATA PADA PYTHON

jika ingin mengambil sebuah tipe data dari variable kita dapat menggunakan function type() 

tipe data yang tersedia di python 
    integer =   bilangan bulat
    float   =   bilangan koma
    String  =   huruf
    boolean =   berisikan True dan False

tipe data khusus biasanya di gunakan untuk seorang ahli matematika atau imajiner
dengan menggunakan method complex(niali1,nilai2) 
    a = complex(1,3)
    print(a)    =>  1+3j

di python juga bisa menambahkan tipe data lain seperti double,char,long 
dengan cara kita melakukan import library dari ctypes atau dari bahasa pemrograman c
    from ctypes import c_double
    b = double(1.23)

"""

# tipe data Integer
nilai_int = 1
print("Nilai data : ",nilai_int)
print("Bertipe : ",type(nilai_int),"\n")

# tipe data Float
nilai_float = 1.2
print("Nilai data : ",nilai_float)
print("Bertipe : ",type(nilai_float),"\n")

# tipe data String
nilai_String = "Halo"
print("Nilai data : ",nilai_String)
print("Bertipe : ",type(nilai_String),"\n")

# tipe data Boolean
nilai_boolean = False
print("Nilai data : ",nilai_boolean)
print("Bertipe : ",type(nilai_boolean),"\n")

# tipe data khusus (imajiner)
nilai_ima = complex(3,5)
print("Nilai data : ",nilai_ima)
print("Bertipe : ",type(nilai_ima),"\n")

# tipe data lain(harus melakukan import library)
from ctypes import c_double as double
nilai_double = double(100.123)
print("Nilai data : ",nilai_double)
print("Bertipe : ",type(nilai_double),"\n")


