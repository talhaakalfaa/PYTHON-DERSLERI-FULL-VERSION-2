# def changeName(n):
#     n = 'talha'

# name = 'çağan'
# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara','izmir']
# change(sehirler[:]) # slicing(parçalama)


# print(sehirler)

# def add(*params): ###!!!! liste için kullanıcaksak tek yıldız sayı gibi yani
#     print(params)
#     return sum((params))

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,50,60,10,20))

def displayUser(**args): ###!!!! sözlü şeyler kullancaksak iki yıldız.
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name = 'talha', age = 19, city = 'denizli')
displayUser(name = 'çağan', age = 27, city = 'denizli', phone = '123132')
displayUser(name = 'selin', age = 18, city = 'denizli', phone = '123132', mail = 'selin@gmail.com')

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myFunc(10,20,30,40,50, key1 = 'value 1', key2 = 'value 2')