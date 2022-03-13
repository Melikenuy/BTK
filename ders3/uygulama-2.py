"""kullanıcı adı ve şifre alınız.. kullanıcı adı olarak "admin" şifre olarak 123456 girilince "sisteme hesaplaıryala giriş yaptınız " yazsın
yanlış girilince "kulllanıcı adı veya şifre yanlış girildi " yazsın tekrar kullankıcı adı ve şifre sorsun """
while True:
    ka=input("kullanıcı adınız: ")
    ş=input("şifreniz: ")
    if ka=="admin" and ş=="123456":
            print("sisteme hesaplarıyla giriş yaptınız")
            break
    else:
        print("kullanıcı adı veya şifre yanlış gitrildi")
        