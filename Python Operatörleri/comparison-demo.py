# 1- Girilen 2 sayıdan hangisi büyüktür ?

# a = int(input('a: '))
# b = int(input('b: ')) 
# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplaınız
# eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# vize1 = float(input('1. vize: '))
# vize2 = float(input('2. vize: '))
# final = float(input('final: '))
# ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
# print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama >= 50}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# sayi = int(input('sayı: '))
# tekcift = (sayi % 2 == 0)
# print(f'girilen sayı çift olma durumu: {tekcift}')

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

# sayi = int(input('sayı: '))
# pozitifmi = (sayi > 0)
# print(f'girilen sayının pozitif olma durumu: {pozitifmi}')


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email:talhakalfa24@gmail.com password:1234)

email = 'talhakalfa24@gmail.com'
password = '1234'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')
istenenEmail = (email == girilenEmail)
istenenPassword = (password == girilenPassword)
print(f'Email bilgisi doğrumu: {istenenEmail} ve Parola doğru mu: {istenenPassword} ')