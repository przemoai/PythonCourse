days =['mon','tue','wen','thur','fri','sat','sun']

workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')
print(days)
print(workdays)