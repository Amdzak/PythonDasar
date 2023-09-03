""" 
Mengambil input dari user

untuk mengambil inputan data dari user kita hanya perlu menuliskan ipnut()
lalu untuk nilai di dalam kurung adalah sebuah pertanyaan contoh
    input("Masukan nama anda : ") => akan menghasilkan sebuah output Maukan nama anda

apapun nilai yang kita masukan di dalam input() ini akan bernilai str atau string
jadi kita memerlukan sebuah casting yang akan membantu dalam pemasukan jenis tipenya
lalu jika kita ingin memasukan angka maka kita harus casting terlebih dahulu
    harga = int(input("Masukan harga: ")) => maka akan bernilai int
 """

data = input("nama kamu : ")
print("nilai data: ",data," [tipe]:",type(data))
harga = float(input("masukan harga: "))
harga = int(input("masukan harga: "))
print("nilai data: ",harga," [tipe]:",type(harga))

