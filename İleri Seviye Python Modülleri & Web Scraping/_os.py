import os 
import datetime

result = dir(os)
result = os.name
#***DİZİN DEĞİŞTİRME***
# os.chdir('C:\\') chdir dosyaları kontrol etmememizi sağlar.
# os.chdir('../..') 

#***KLASÖR OLUŞTURMA***
# os.mkdir("newdirectory") mkdir dosya açmak için kullanılır.
# os.makedirs("newdirectory/yeniklasör") makedirs iç içe klasör oluşturur.
# os.rename("newdirectory","yeniklasör") klasör adını değiştirmeye yarar
# os.rmdir("newdirectory") rmdir alt klasör olmadığında klasörü silmeye yarar.
# os.removedirs("yeniklasör/yeniklasör") alt klasörleri olan dosyalar için kullanılır.

#***LİSTELEME***
# result = os.listdir() şuan etkin olan dizin içindeki klasörleri gösterir.
# result = os.listdir('C:\\') C diskinin içindeki klasörleri listeledi.
# for dosya in os.listdir():
#     if dosya.endswith('py'): endswith dosyanın sonundaki bir bilgisi için işe yarar.
#         print(dosya)

#***ETKİN DİZİN ÖĞRENME***
# result = os.getcwd() # getcwd bu yazdığımız kod hangi dosyanın içinde olduğunu verir.

# result = os.stat("date.py")
# result = result.st_size/1024
# result =datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihini verir.
# result =datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihini verir.
# result =datetime.datetime.fromtimestamp(result.st_mtime) # değiştirilme tarihini verir.

# os.system("notepad.exe") system windows üzerinden uygulama açmayı sağlar.

#***path dosyanın uzantısını ya da ismini nasıl değitirirsin gibi şeylerde kullanılır path***

# result = os.path.abspath("_os.py") #abspath ile dosyanın tam konumu alınır.
# result = os.path.dirname("C:/Users/Talha/Desktop/python_temelleri/_os.py") #dirname dizin ismini almasını sağlar
# result = os.path.dirname(os.path.abspath("_os.py"))
# result = os.path.exists("_os.py") #exists böyle bir dosya ya da klasör var mı diye sorgular
# result = os.path.isdir("C:/Users/Talha/Desktop/python_temelleri/_os.py") #isdir klasör mü değil mi diye kontrol eder.
# result = os.path.isfile("C:/Users/Talha/Desktop/python_temelleri/_os.py") #isfile dosya mı değil miye kontrol eder.
# result = os.path.join("C:\\","deneme","deneme1") #join birleştirmek için kullanılır.
# result = os.path.split("C:\\deneme") #split ayırmak için kullanılır
# result = os.path.splitext("_os.py") #splittext dosyanın ismi ile uzantısını ayrı ayrı vermek için kullanılır.
# result = result[0] çıktısı os verir


print(result)
