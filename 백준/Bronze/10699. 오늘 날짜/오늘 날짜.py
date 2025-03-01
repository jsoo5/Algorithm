import datetime

kst = datetime.datetime.today()
utc = datetime.timedelta(hours=9)
result = kst - utc

print(result.strftime('%Y-%m-%d'))