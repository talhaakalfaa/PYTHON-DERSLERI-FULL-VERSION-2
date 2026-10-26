def sayHello(name = 'user'):
   return 'Hello '+ name

msg = sayHello('Talha')

print(msg)


def total(num1, num2):
   return num1 + num2

result = total(15,35)
result = total(15,17)

print(result)

def yasHesapla(dogumYili):
   return 2025 - dogumYili

age = yasHesapla(2006)
print(age)

def EmekliligeKacYilKaldi(dogumYili, isim):
   yas = yasHesapla(dogumYili)
   emeklilik = 65 - yas

   if emeklilik > 0:
      print(f'emekliliğinize {emeklilik} yıl kaldı')
   else:
      print('zaten emekli oldunuz.')

EmekliligeKacYilKaldi(2006, 'Talha')