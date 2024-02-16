import time
from datetime import datetime, date, timezone, timedelta

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
     now = time.time()
     return now

def tuple_time_now():
     now = stuff
     return now

def future_time_unix (timeadder):
     now = unix_time_now
     future = unix_time_now + timeadder
     return future
