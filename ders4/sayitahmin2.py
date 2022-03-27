
import random
while True:
    seviye=input("bir seviye seçiniz kolay/orta/zor :")
    if seviye=="kolay":
        uret=random.randint(1,10)
        break
    elif seviye=="orta":
        uret=random.randint(1,50)
        break
    elif seviye=="zor":
        uret=random.randint(1,100)
        break
    else :
        print("lütfen doğru seçim yapınız ")

while True:
    tahmin=int(input("bir tahminde bulumuz :"))
    if tahmin<uret:
        print("sayıyı büyültün")
    elif tahmin>uret:
        print("sayıyı küçültün")
    else:
        print("tebrikler,bildiniz!")
        break
