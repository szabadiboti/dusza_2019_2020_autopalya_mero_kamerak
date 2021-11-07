from constants import *


road = (POSITIONS[2]-POSITIONS[0])*1000

on_all = {}


def run(read, i):
    l = read.t + "_" + read.code + "_" + read.license
    if l not in on_all:
        on_all[l] = [-1, -1]
    if read.thing == "A":
        on_all[l][0] = read.seconds
    elif read.thing == "C":
        on_all[l][1] = read.seconds


def finish():
    s = []
    for key in on_all:
        if -1 not in on_all[key]:
            car = key.split("_")
            limit = LIMITS[car[0]]
            times = on_all[key]
            time = times[1]-times[0]
            speed = (road/time)*3.6
            s.append(f"{'igen' if speed <= limit else 'nem'} {car[1]} {car[2]}")
    return "\n".join(s)
