""" 
    String & STRING METHOD

    didalam python kita dapat menggunakan string dengan cara membuat single quote '....' 
                                                                     atau double "...."
    didalam penggunakan string juga memiliki beberapa function seperti 
    len()       untuk mengetahui panjang dari baris tersebut
    in          untuk mengecek apakaha ada kata yang cocok didalam nya
    print(r"")  untuk melakukan print raw yang mana akan membuat semua tulisan menjadi seperti apa yang ada misal \n akan mencaji tulisan \n bukan sebuah enter
    \n          untuk membuat new line system operasi unix LF
    \r          untuk membuat return atau new line tetapi untuk bahada pemograman lama
    \t          untuk membuat sebuah tab atau indentasi
    \r\n        untuk membuat new line tetapi untuk sistem windows CRLF

    []      penggunaan index juga bisa untuk string yang mana akan mencari nilai berdasarkan indexnya
            jika di isi - maka akan mencari mulai belakang
            jika di isi : jika di isi 2 0:3 maka akan mengambil sampai tetapi nilai akhir tidak di ikut sertakan 
            jika di isi : nilainya ada 3 0:5:3 (nilai awal:nilai akhir:increment atau lompat)
    min()   mengambil nilai paling kecil dari assci code
    max()   mengambil nilai paling besar dari acsii code
    count() menghitung jumlah yang ada 

    STRING METHOD
    ada beberapa method dalam string yang sangat berguna 
    "".join(data)          untuk melakukan join pada suatu tulisan bisa di gunakan pada list
    .split(separator)      untuk membuat tulisan menjadi list dan di pisah berdasarkan separator tertentu
    .uper()                untuk melakukan uppercase sebuah tulisan
    .lower()               untuk melakukan lowercase sebuah tulisan
    .center(int,data)      untuk membuat tulisan bisa rata tengah jika data di isi maka akan menghasilkan nilai bebas jika int di isi maka akan membuatakan sebuah spasi sesui keiginan
      .rjust               sama seperti center tapi dia rata kanan (right)
      .ljust               sama seperti ljust tapi dai rata kiri (left)
"""

nama = 'Amdzak'
panjang = len(nama)

print("Panjang dari kalimat "+nama +" = "+str(panjang)) # harus di casting str karena operasi penggabungan hanya bisa untuk string
print(r"Halo \n \t \r\n <-- mejadi tulisan biasa karen aada print(r'...')")

tujuan = "md"
ada = tujuan in nama

print("apakah " + tujuan +" ada di dalam nama Amdzak? " + str(ada))

nama = "Kucing Salto haha"
print("huruf terakhir di nama Kucing Salto adalah " + nama[-1])
print("index ke 0 sampai 4 dari nama Kucing Salto =  " + nama[0:4])
print("index ke 0 sampai terakhir tetapi loncat 2 dari nama Kucing Salto =  " + nama[0:-1:2])

hitung = nama.count("a") # akan menghitung suatu nilai yang ada pada isian tertenru
print(hitung)


# METHOD STRING
data1 = "halooo"
uper = data1.upper()
print(uper)

data = "KUCING SALTO"
lower = data.lower()
print(lower)

data2 = ["kucing","Salto","kucing"]
join = " ".join(data2)
print(join)

data3 = "kucing lompat kucing hewan"
split = data3.split(" ")
print(split)

data4 = "Selamat Datang"
center = data4.center(20,"=")
print(center)

ljust = data4.ljust(20,"#")
print(ljust)

rjust = data4.rjust(20,"#")
print(rjust)