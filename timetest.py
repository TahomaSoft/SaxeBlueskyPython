#!/usr/bin/python

"""
Time tester
"""

from ticktocktime import bsky_time_now,unix_time_now,future_time_unix,tuple_time2dt,tuple_time_now, iso2unix_time
from ticktocktime import iso_time_now, iso2tuple_time, iso2unix_time

x = bsky_time_now()

f = iso_time_now()
print ("iso time: \n", f)

y = unix_time_now()

z = future_time_unix(10)



ttouple = tuple_time_now()

niftytime = tuple_time2dt (ttouple)

newtuple = iso2tuple_time (f)

print ("New tuple: \n", newtuple)

a = iso2unix_time(f)

print (a)

