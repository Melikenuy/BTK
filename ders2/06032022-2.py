liste=[]#boş bir liste tanımlanır
liste=["elma","armut",20]#artık listenin elemnaları değişti!
sayilar=[15,19,12,2,45,6,7]
isimler=["hatice","beyza","zehra","zeynep","nur"]
gunler=["pazartesi","salı","çarşamba"]
print(gunler)
print("0.indeksdeki eleman:",gunler[0])
print("1.indeksdeki eleman:",gunler[1])
print("2.indeksdeki eleman:",gunler[2])
gunler.append("perşembe")
print(gunler)
print ("eleman sayısı : ",len(gunler))# listenin eleman sayısını verir
gunler.pop(0)
print(gunler)
gunler.clear()
print(gunler)
print(sayilar)
sayilar.sort()#boş bırakıldığı halde küçükten büyüğe sıralar
print("küçükten büyüğe sıralı:",sayilar)
sayilar.reverse()#tersten yazdırır
print("büyükten küçüğe sıralı:",sayilar)
isimler.sort()
print("alfabetik sıralı:",isimler)
isimler.reverse()
print("alfabetik tersten sıralı:",isimler)


