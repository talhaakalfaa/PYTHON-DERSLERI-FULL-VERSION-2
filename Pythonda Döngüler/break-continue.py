# name = 'talha kalfa'

# for letter in name:
#     if letter == 'k':
#         break
#     print(letter)

# x = 0
# while x < 5:
#     x +=1
#     if x == 2:
#         continue
#     print(x)


# 1-100 e kadar tek sayıların toplamı 

# x = 1
# result = 0

# while x <= 100:
#     x +=1
#     if x % 2 ==0:
#         continue
#     result += x
    

# print(f'toplam: {result}')



n = int(input())
# Write your code below
for i in range(1,n+1):
    for j in range(1,n+1):
        if i * j == n:
            print(i,j)