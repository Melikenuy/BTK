# kendisine gönderilen kulllanıcı adı ve şifreyi kontrol ederek sonucunda true yada false
# gönderen fonksiyonun python kodu kullanıcı adı: admin ,şifre:123456 olamalı.

def kontrol(a,s):
    if k=="admin" and s=="123456":
        return True
    else:
        return False
k=input("kulllanımcı adı: ")
s=input("şifre:")
sonuc=kontrol(k,s)
print(sonuc)

if sonuc=="True":
    print("doğru giriş")
else:
    print("kullanıcı adı yad aşifre yanlış.")