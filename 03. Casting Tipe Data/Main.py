""" 
Casting

casting adalah merubah tipedata menjadi tipedata lain

untuk casting ke boolean nilai akan menjadi false jika 0 dan akan menjadi true dengan nilai selain 0
berlaki juga untuk string to boolean jika ada isinya maka bernilai true dan jika kosong maka bernilai false
untuk cating dari float ke int dia akan melakukan convert ke bawah walaupun nilainya 10.99 AKAN BERNILAI 10 
 """


print("==FROM INTEGER TO ANY")
nilai_data = 10
print("Nilai Awal = ",nilai_data," Tipe Awal: ",type(nilai_data))
dataFloat  = float(nilai_data)
dataString = str(nilai_data)
dataBool   = bool(nilai_data)

print("nilai = ",dataFloat," jenis :",type(dataFloat))
print("nilai = ",dataString," jenis :",type(dataString))
print("nilai = ",dataBool," jenis :",type(dataBool))


print("==FROM FLOAT TO ANY")
nilai_float = 10.12
print("Nilai Awal = ",nilai_float," Tipe Awal: ",type(nilai_float))
dataInt    = int(nilai_float)
dataString = str(nilai_float)
dataBool   = bool(nilai_float)

print("nilai = ",dataInt," jenis :",type(dataInt))
print("nilai = ",dataString," jenis :",type(dataString))
print("nilai = ",dataBool," jenis :",type(dataBool))


print("==FROM BOOLEAN TO ANY")
nilai_bool = True
print("Nilai Awal = ",nilai_bool," Tipe Awal: ",type(nilai_bool))
dataInt     = int(nilai_bool)
dataString  = str(nilai_bool)
dataBool    = bool(nilai_bool)

print("nilai = ",dataInt," jenis :",type(dataInt))
print("nilai = ",dataString," jenis :",type(dataString))
print("nilai = ",dataBool," jenis :",type(dataBool))


print("==FROM STRING TO ANY")
nilai_str = "adalah Benar" #jika nilainya angka tidak error dan jika nilainya "" maka akan menjadi false
print("Nilai Awal = ",nilai_str," Tipe Awal: ",type(nilai_str))
# dataInt     = int(nilai_str)
# dataFloat   = float(nilai_str)
dataBool    = bool(nilai_str)

# print("nilai = ",dataInt," jenis :",type(dataInt))
# print("nilai = ",dataFloat," jenis :",type(dataFloat))
print("nilai = ",dataBool," jenis :",type(dataBool))