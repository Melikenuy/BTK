try:

    sayi=int(input("bir dayı giriniz : "))
    sayi2=int(input("bir dayı giriniz : "))
    print ("bölüm :",sayi/sayi2)

 except ValueError:
     print("lütfen sayı giriniz !!! ")
    except ZeroDivisionError:
        print("0'a bölme yapılamaz!")
    except SyntaxError:
        print("yazım hatan var")
    except NameError:
        print("böyle bir değişken yok")
    except :
        print("genel hatan var")
    print("program buradan devam eder")