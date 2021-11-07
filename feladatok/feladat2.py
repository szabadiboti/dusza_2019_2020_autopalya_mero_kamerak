from constants import *

infractions = []


def run(read, i):
    if read.thing != 'B':
        return
    if read.t in ['sz', 'm'] and read.speed > MAX_MOTOR:
        infractions.append(" ".join([read.t, read.code, read.license, str(read.speed - MAX_MOTOR)]))
    if read.t == 'b' and read.speed > MAX_BUS:
        infractions.append(" ".join([read.t, read.code, read.license, str(read.speed - MAX_BUS)]))
    if read.t == 't' and read.speed > MAX_TRUCK:
        infractions.append(" ".join([read.t, read.code, read.license, str(read.speed - MAX_TRUCK)]))


def finish():
    return '\n'.join(infractions)
