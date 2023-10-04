""" 
Format String 

Format string merupakan sebuah cara untuk mempermudah penulisan 
yaitu dengan menambhakan huruf f di depan seperti :
    a = 10
    b = f "nilai dari angka 1 = {a}"
 jadi dengan menggunakan format string akan lebih memudahkan kita dalam melakukan pemanggilan variable
"""

""" INT
:d untuk menandakan bahwa nilai dari bilangan terbeut ada bilangan bulat"""
nilai1 = 10
print(f"nilainya adalah = {nilai1:d}")

""" BOOLEAN """
boo = True
print(f"nilainya adalah = {boo}")

""" String """
str = "not hehe"
print(f"nilainya adalah = {str}")

""" float """
flt = 12.31
print(f"nilainya adalah = {flt}")

""" bilangan ribuan  
    menambahkan :, maka akan membuat secara otomatis koma dengan cara ribuan atau 3 digit"""
rb = 20000
print(f"nilainya adalah = {rb:,}")

""" bilangan koma
    menambahkan :.angkaf yang dimana angaka di ganti sebarap banya digit yg ingin di ambil """
km = 123.3123
print(f"nilainya adalah = {km:.2f}")