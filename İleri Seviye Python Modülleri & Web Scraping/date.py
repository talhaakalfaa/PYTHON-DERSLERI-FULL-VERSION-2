# from datetime import datetime = datetime.datetime
# from datetime import date = datetime.date
# from datetime import time  = datetime.time

# import datetime

from datetime import datetime
from datetime import timedelta

simdi = datetime.now()
simdi = datetime.today()


result = datetime.now()
result = simdi.hour
result = simdi.day
result = simdi.minute
result = simdi.month
result = simdi.second
result = simdi.year

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y') #Y year
result = datetime.strftime(simdi,'%X') # X hour
result = datetime.strftime(simdi,'%d') # ayın kaçı olduğunu verir
result = datetime.strftime(simdi,'%A') # A günü string olarak verir
result = datetime.strftime(simdi,'%B') # B ayı string olarak verir
result = datetime.strftime(simdi,'%Y %B %A')

t = '15 April 2025 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S' ) 
result = result.year

birthday = datetime(2006,5,24,12,30,10)

result = datetime.timestamp(birthday) # tarihi saniye bilgisi olarak verir alttakinin tersi 
result = datetime.fromtimestamp(result) # saniyeyi tarihe çevirir yani üsttekinin tersi oluyor 
result = datetime.fromtimestamp(0)

result = simdi - birthday # timedelta objesi gelir sonuç.

# result = result.days 
# result = result.seconds
# result = result.microseconds
print(simdi)

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes = 10)

result = simdi - timedelta(days = 10)

print(result)

