# kullanıcıdan  harf girmesini isteyiniz  e girerse erkek k girerse kadın yazdırınız
print("HOŞGELDİNİZ")
harf=input("E veya K harfini giriniz:")
if harf == "E" or harf == "e":
    print("Erkek")
elif harf == "K" or harf == "k":    #2. veya daha fazla şartlarda kullanılır
    print("Kadın")
else :
    print( "lütfen E/K harflerini giriniz")
print( "HOŞÇAKAL...")