#FONKSİYONLAR

#Toplama
def toplama(x,y):
    return x+y
#Çıkarma işlemi
def cikarma(x,y):
    return x-y
#Bölme işlemi
def bolme(x,y):
    return x/y
#Çarpma işlemi
def carpma(x,y):
    return x*y


#Ekrana bastırılacak kısım
print("------------------------------------")
print("HOŞGELDİNİZ")
print("HESAP MAKİNESİ")
print("------------------------------------")


#KULLANICI GİRİŞİ
islem=input("İşlem seçiniz (+,-,*,/) > ")
sayi1=float(input("Birinci sayı > "))
sayi2=float(input("İkinci sayı > "))
print("------------------------------------")

#Sonuç atamaları
if islem=="+":
    print(sayi1,"+",sayi2,"=",toplama(sayi1,sayi2))

elif islem=="-":
    print(sayi1,"-",sayi2,"=",cikarma(sayi1,sayi2))

elif islem=="*":
    print(sayi1,"x",sayi2,"=",carpma(sayi1,sayi2))

elif islem=="/":
    print(sayi1,"/",sayi2,"=",bolme(sayi1,sayi2))
#Farklı bir işlem girilecek olursa
else:
    print("HATALI GİRİŞ YAPTINIZ!")




