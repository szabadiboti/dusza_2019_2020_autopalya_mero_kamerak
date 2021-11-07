from constants import *

n = 0


def run(read, i):
    global n
    if read.t == 'm' and read.speed > MAX_MOTOR:
        n += 1


def finish():
    return n
