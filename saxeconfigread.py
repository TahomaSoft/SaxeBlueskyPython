#!/usr/bin/python3

import toml
import time
from datetime import date, datetime, timezone

mainconfigfile_name = './saxe-main.toml'
with open(mainconfigfile_name, 'r') as mainconfigfile:
    toml_in = toml.load(mainconfigfile)
    mainconfigfile.close

# print (toml_in)

# outfile_name = './salt-main.toml'

# with open(outfile_name, 'w') as outfile:
#    toml.dump(toml_in, outfile)


stateconfigfile_name = './saxe-state.toml'
with open (stateconfigfile_name, 'r') as stateconfigfile:
    statetoml_in = toml.load(stateconfigfile)
    stateconfigfile.close()

statetoml_in['BSKY_INFO']['previous_last_posted_unix'] \
    = statetoml_in['BSKY_INFO']['last_posted_unix']
statetoml_in['BSKY_INFO']['previous_last_posted_iso'] = \
     statetoml_in['BSKY_INFO']['last_posted_iso']

# now_iso = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
now_iso = datetime.now(timezone.utc).isoformat()
now_unix = time.time()

statetoml_in['BSKY_INFO']['last_posted_unix'] = now_unix
statetoml_in['BSKY_INFO']['last_posted_iso'] = now_iso


stateoutfile_name = './saxe-state.toml'

with open(stateoutfile_name, 'w') as stateoutfile:
    toml.dump(statetoml_in, stateoutfile)
    stateoutfile.close()
