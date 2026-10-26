import requests #requests modülü, Python’da internet üzerinden veri almak veya göndermek için kullanılan en popüler kütüphanedir.
import json


api_key = "d396adfe32bef01128cb89c3"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("bozulan döviz türü: ") #USD
alınan_doviz = input("alınan döviz türü: ") #TRY
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ")) # ne kadar USD

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

# print(sonuc_json["conversion_rates"][alınan_doviz])

print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alınan_doviz], alınan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * sonuc_json["conversion_rates"][alınan_doviz], alınan_doviz))