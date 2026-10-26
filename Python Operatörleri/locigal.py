x = 5
result = 5 < x < 10
hak = 0
devam ='e'
# and kullandığımızda !!! iki soruda True ise => True olur. !!! Biri True biri false ise => False olur !!!

result = (x > 5) and (x < 10)
result = (hak > 0) and (devam == 'e')

# or kullandığımızda !!! iki soruda True ise => True , Biri True biri False ise => True , ikiside False ise => False
 
result = (x > 0) or (x % 2 == 0)

# not

result = not(x > 0) # (x > 0) normalde True ama not tam tersini veriyor yani False veriyor.

# x, 5-10 arasında olan bir çift sayı mı?

result = ((x>5) and (x<10)) and (x%2==0)

print(result)