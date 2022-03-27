# dikdörtgenin alanını ve çevresini hesaplayan 2 ayrı foksiyon yazınız.
# kullanıcıdan aldığınz değere göre alanı ve çevreyi ekrana yazınız.
def alan(a,b):
    return a*b
def cevre(a,b):
    return (a+b)*2
d=int(input("uzun kenar:"))
c=int(input("kısa kenar:"))
print("dikdörtgenin alanı:",alan(d,c))
print("dikdörtgenin çevresi",cevre(d,c))

