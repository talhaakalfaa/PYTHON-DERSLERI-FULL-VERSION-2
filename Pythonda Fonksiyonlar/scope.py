# global scope
x = 'global x'

def function(): 
    #local scope 
    x = 'local x'
    print(x) # fonksiyon içinde print(x) yazarsan 'local x' yazdırır.

function()
print(x) # fonksiyon dışında print(x) yazarsan 'global x' yazdırır.

#############################

# global
name = 'Talha'

def changeName(new_name):
    #local
    global name
    name = new_name
    print(name)

changeName('Çağan')
print(name)
##############################

name = 'global string'

def greeting():
    # name = 'talha'

    def hello():
        # name = 'çağan'
        print('hello ' + name)

    hello()

greeting()
##############################

x = 50
def test():
    global x
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)