from datetime import  datetime, date, timezone, timedelta
from time import time, gmtime, strptime, strftime

def bsky_time_now():
     now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
     return now

def iso_time_now():
     now = datetime.now(timezone.utc).isoformat()
     return now

def iso_time_future(addSeconds):
      now = datetime.now(timezone.utc).isoformat()
      future = now + timedelta (seconds=addSeconds)
      return future

def unix_time_now():
     now = time()
     return now

def tuple_time_now():
     now = gmtime()
     return now

def tuple_time2dt (tupleTime):
     s = tupleTime
     dt = datetime(*s[:6], tzinfo=timezone.utc) # iterated unpacking
     return (dt) # a datetime.datetime object, ISO-ish human readable date/time

def tuple_time2unix (tupleTime):
     import time
     import calendar
     unixtime = calendar.timegm(tupleTime)
     return unixtime

def future_time_unix (timeadder): # add now as first of 2 params
     now = unix_time_now()
     future = now + timeadder
     return future

def iso2tuple_time (thetime):
     import time
     tupletime = time.strptime(thetime, "%Y-%m-%dT%H:%M:%S.%f%z")
     return tupletime

def iso2unix_time (iso_time):
     import time
     import calendar
     # With fractional seconds
     # unixtime  = datetime.timestamp (datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%S.%f%z"))
     # or without fractional seconds
     temp = iso2tuple_time (iso_time)
     unixtime = calendar.timegm(temp)     
     return unixtime
