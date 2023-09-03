""" 
Operasi komparasi

hasil keluaran dari operator komparasi adlah boolean True atau False
operasi komparasi di python sama seperti di bahasa pemrogrmana lainya yaitu 
    ==      :   sama dengan
    !=      :   tidak sama dengan
    >       :   lebih dari
    <       :   kurang dari
    >=      :   lebih dari sama dengan
    <=      :   kurang dari sama dengan

ada beberapa operator komparasi baru 
    is      :   untuk membandingkan antara 2 buah object apakah nilai alamatnya sama 
    is not  :   kebalikan dari is
"""

a = 5
b = 4

# komparasi sama dengan
hasil = a == b
print(a,"==",b," : ",hasil)

# komparasi Lebih dari
hasil = a > b
print(a,">",b," : ",hasil)

# komparasi  Kurang dari
hasil = a < b
print(a,"<",b," : ",hasil)

# komparasi leboh dari sama dengan
hasil = a >= b
print(a,">=",b," : ",hasil)

# komparasi Kurang dari sama dengan
hasil = a <= b
print(a,"<=",b," : ",hasil)

# komparasi Tidak sama dengan
hasil = a != b
print(a,"!=",b," : ",hasil)

# komparasi dengan is yaitu membandingkan 2 buah object

c = 8
d = 9

hasil = c is d #tidak di sarankan jika c is 9 
print(c,"is",d," : ",hasil)

hasil = c is not d #tidak di sarankan jika c is not 9 
print(c,"is not",d," : ",hasil)