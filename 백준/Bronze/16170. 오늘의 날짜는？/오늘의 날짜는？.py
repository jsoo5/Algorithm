import datetime

date = datetime.datetime.utcnow()
only_date = str(date).split()[0]
result = only_date.split('-')

for i in result:
    print(i)