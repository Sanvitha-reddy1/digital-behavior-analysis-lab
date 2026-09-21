import random
import datetime
#print(random.seed.__doc__)

#print(datetime.timedelta.__doc__)

x = 10

p = datetime.datetime.now()
q = datetime.timedelta(days = x)
print(p+q)
