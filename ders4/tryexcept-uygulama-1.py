# kulllanıcıdan bir sayı girmesini isteyen  sayı girmediğinde tekrar tekrar sayı
# girmesini isteyen sayı girdiğinde de ekrana sayının mkaresinli yazdıran program
while True:
    try:
        s=int(input("bir sayı giriniz: "))
        break
    except ValueError:
        print ("lütfen bir sayı giriniz!!!")

print("karesi:",s**2)

