import datetime
dt=datetime.datetime.now()
specal = dt.strftime("%A, %d.%B %Y %I:%M%p")
#print(dt)
#print(specal)
timing ='Today is {0:%A},The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}'.format(dt,"date","month","time")