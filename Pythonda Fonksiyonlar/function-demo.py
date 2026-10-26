# 1- Gönderilen bir kelimeye belirtilen kez ekranda gösteren fonksiyonu yazın.

# def yazdır(kelime, adet):
#     print(kelime * adet)
# yazdır('merhaba canım\n', 10)


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazın.

# def listeyeCevir(*params):
#     liste = []
#     for param in params:
#         liste.append(param)

#     return liste

# result = listeyeCevir(10,20,30,'Merhaba')
# print(result)




# 3- Gönderilen 2 asal sayı arasınaki tüm asal  sayıları bulun.
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde fonksiyondan geri gönder.


# def tamBolenleriBul(sayi):
#     tamBolenler = []

#     for i in range(2, sayi):
#         if (sayi % i == 0):
#             tamBolenler.append(i)
    
#     return tamBolenler

# print(tamBolenleriBul(90))