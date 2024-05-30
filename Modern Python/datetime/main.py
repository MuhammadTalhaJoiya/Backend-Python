from datetime import datetime, timedelta

# def func1(exptime: timedelta):
#     expire = datetime.now() + exptime  # Using the exptime parameter passed to the function
#     return expire

# Define the timedelta
print(timedelta(minutes=1))
print(datetime.now())
print(datetime.now()+timedelta(minutes=1))

# Call func1 with the timedelta parameter

def func():
    time=datetime.now()+timedelta(seconds=30)
    data={"time":time,"Hello":"Pakistan"}
    return data

print(func())
# it will not expire because it is not token