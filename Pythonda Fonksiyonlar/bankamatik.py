# Bankamatik Uygulaması

TalhaHesap = {
    'ad': 'Talha Kalfa',
    'hesapNo':'12345678',
    'bakiye': 3000,
    'ekHesap':2000
}

CaganHesap = {
    'ad': 'Çağan Kalfa',
    'hesapNo':'11223344',
    'bakiye': 2000,
    'ekHesap':1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilrisiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızada {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınzıda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(TalhaHesap, 3000)

print('***********')
paraCek(TalhaHesap, 2000)
