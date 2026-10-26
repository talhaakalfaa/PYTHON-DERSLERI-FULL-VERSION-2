# # 1-100 e kadar 

# x = 1

# while x <= 100:
#     if x % 2==1:
#         print(f'{x} tek sayı.')
#     else:
#         print(f'{x} çift sayı.')
#     x += 1

# print('Bitti...')

name = '' #False
while not name.strip():
    name = input('isminizi giriniz: ')

print(f'Merhaba, {name}')