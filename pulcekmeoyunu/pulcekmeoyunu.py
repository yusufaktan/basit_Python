print("SON PULU CEKEN KAZANIR !\n--------" )
x=int(input("Cekilecek toplam pul sayisi :"))
y=int(input("Cekilecek maksimum pul sayisi :"))
print("--------\nOYUN BASLADI\n--------")

def pul_kaldirma_oyna (x,y):
    while x>0:
        oyuncu1=int(input("1. oyuncu kac pul cekmek istiyorsun ? ="))
        while (oyuncu1<=0 or oyuncu1>y):
            if oyuncu1>y:
                print("Maksimum pul sayisindan fazla pul cekemezsin")
            oyuncu1=int(input("1. oyuncu kac pul cekmek istiyorsun ? ="))
        x=x-oyuncu1
        print("Kalan pul sayisi =",x)
        if(x<=0):
            print("1. oyuncu\nKAZANDINIZ!")
            break

        oyuncu2=int(input("2. oyuncu kac pul cekmek istiyorsun ? ="))
        while (oyuncu2<=0 or oyuncu2>y):
            if oyuncu2>y:
                print("Maksimum pul sayisindan fazla pul cekemezsin")
            oyuncu2=int(input("2. oyuncu kac pul cekmek istiyorsun ? ="))
        x=x-oyuncu2
        print("Kalan pul sayisi",x)
        if(x<=0):

            print("2. oyuncu\nKAZANDINIZ!")

if x<=0:
    print("Lutfen sifirdan buyuk bir sayi giriniz.")

pul_kaldirma_oyna(x,y)