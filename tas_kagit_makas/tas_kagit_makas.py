import random

print("HOŞGELDİN\n!! 3 OLAN KAZANIR !!\n============================")
oyuncu=0
bot=0

while True:
    print("> Taş       [1]\n> Kağıt     [2]\n> Makas     [3]")
    oSecim = input(">> Seçimini yap > ")
    print("============================")
    bSecim = random.choice(["1", "2", "3"])

    if oSecim == "1":
        if bSecim == "1":
            print("Rakibinin seçimi : Taş\nBerabere !")
            print("Durum > ",oyuncu," - ",bot,"\n============================")

        elif bSecim == "2":
            print("Rakibinin seçimi : Kağıt\nKaybettin !")
            bot += 1
            print("Durum > ", oyuncu, " - ", bot, "\n============================")
            if(oyuncu==3):
                print("KAZANDIN !!")
                break
            elif(bot==3):
                print("KAYBETTİN !!")
                break

        elif bSecim == "3":
            print("Rakibinin seçimi : Makas\nKazandın !")
            oyuncu += 1
            print("Durum > ", oyuncu, " - ", bot, "\n============================")
            if (oyuncu == 3):
                print("KAZANDIN !!")
                break
            elif (bot == 3):
                print("KAYBETTİN !!")
                break


    elif oSecim == "2":
        if bSecim == "1":
            print("Rakibinin seçimi : Taş\nKazandın !")
            oyuncu += 1
            print("Durum > ", oyuncu, " - ", bot, "\n============================")
            if (oyuncu == 3):
                print("KAZANDIN !!")
                break
            elif (bot == 3):
                print("KAYBETTİN !!")
                break

        elif bSecim == "2":
            print("Rakibinin seçimi : Kağıt\nBerabere !")
            print("Durum > ", oyuncu, " - ", bot, "\n============================")
            if (oyuncu == 3):
                print("KAZANDIN !!")
                break
            elif (bot == 3):
                print("KAYBETTİN !!")
                break

        elif bSecim == "3":
            print("Rakibinin seçimi : Makas\nKaybettin !")
            bot += 1
            print("Durum > ", oyuncu, " - ", bot, "\n============================")
            if (oyuncu == 3):
                print("KAZANDIN !!")
                break
            elif (bot == 3):
                print("KAYBETTİN !!")
                break

    elif oSecim == "3":
        if bSecim == "1":
            print("Rakibinin seçimi : Taş\nKaybettin !")
            bot += 1
            print("Durum > ", oyuncu, " - ", bot, "\n============================")
            if (oyuncu == 3):
                print("KAZANDIN !!")
                break
            elif (bot == 3):
                print("KAYBETTİN !!")
                break

        elif bSecim == "2":
            print("Rakibinin seçimi : Kağıt\nKazandın !")
            oyuncu += 1
            print("Durum > ", oyuncu, " - ", bot, "\n============================")
            if (oyuncu == 3):
                print("KAZANDIN !!")
                break
            elif (bot == 3):
                print("KAYBETTİN !!")
                break

        elif bSecim == "3":
            print("Rakibinin seçimi : Makas\nBerabere !")
            print("Durum > ", oyuncu, " - ", bot, "\n============================")
            if (oyuncu == 3):
                print("KAZANDIN !!")
                break
            elif (bot == 3):
                print("KAYBETTİN !!")
                break

    else:
        print("Hatalı giriş yaptın. Lütfen tekrar oyna...")
        break

