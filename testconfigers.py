import toml
from datetime import date, datetime, time, timezone


def readMainConfig (mainconfigfile_name):

    with open(mainconfigfile_name, 'r') as mainconfigfile:
        toml_in = toml.load(mainconfigfile)

    mainconfigfile.close()
    return toml_in

def readStateConfig (stateconfigfile_name):

    with open (stateconfigfile_name, 'r') as stateconfigfile:
        statetoml_in = toml.load(stateconfigfile)

    stateconfigfile.close()
    return statetoml_in


def writeStateConfig (stateoutfile_name, stateData2write):
    with open(stateoutfile_name, 'w') as stateoutfile:
        toml.dump(stateData2write, stateoutfile)
    stateoutfile.close()
    



