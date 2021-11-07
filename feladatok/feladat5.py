from constants import MAX_MOTOR

infractions = []


def run(read, i):
    if read.t == 'sz' and read.thing == 'C' and 9 <= read.date.hour < 13 and 110 < read.speed < MAX_MOTOR:
        infractions.append(" ".join([read.code, read.license, str(read.speed), read.time]))


def finish():
    return '\n'.join(infractions)
