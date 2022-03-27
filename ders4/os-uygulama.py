import os
#os.rmdir("elma")
secenek=input("iki seçenekten birini seçiniz : klasör sil / klasör aç ")
if secenek=="klasör sil":
         # adı girilen klasörü silen kodlar
    a=input("silinecek klasör adı giriniz :")
    for i in range(1, 11) :
        os.rmdir(a+str(i))
        print("10 klasör silindi")

elif secenek== "klasör aç":
        # adı girilen klasörden 10 tane oluran kodlar
    a=input("klasör adı yazınız :")
    for i in range (1,11):
        os.mkdir(a+str(i))
        print("10 klasör eklendi")




