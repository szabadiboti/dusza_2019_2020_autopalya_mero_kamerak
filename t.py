from collections import namedtuple
import constants
import sys

positions = []
LETTERS = ("A", "B", "C")

Date = namedtuple("Date", "hour minute second")

"""
code - felségjel
license - rendszám
thing - mérő műszer
t - típus
speed - sebesség :P
time - nyers idő
pos - pozíció a mérő műszer alapján
date - (hour, minute, second)
seconds - mérési idő másodpercekben
"""


class Read:
    def __init__(self, line):
        self._line = line
        self.code, self.license, self.thing, self.t, self.speed, self.time = line.split(",")
        self.speed = int(self.speed)
        self.pos = positions[LETTERS.index(self.thing)-1]
        self.date = Date(*tuple(map(int, self.time.split(":"))))
        self.seconds = self.date.hour*60**2+self.date.minute*60+self.date.second


reads = []
road_code = "M1"  # input("Útvonalkód\n> ")

with open(f'input/{road_code}.txt', 'r') as f:
    positions = list(map(int, f.readline().split(",")))
    l = None
    while l := f.readline():
        reads.append(Read(l.strip()))

constants.POSITIONS = positions[:]
constants.POSITIONS_ABC = {"A": positions[0], "B": positions[1], "C": positions[2]}

override = sys.argv[1:] if len(sys.argv) > 1 else []

_feladatok = [(n, getattr(__import__(f"feladatok.feladat{n}"), f"feladat{n}")) for n in (override if override else range(1, 11))]

for i in range(len(reads)):
    for feladat in _feladatok:
        feladat[1].run(reads[i], i)

out = ""

for feladat in _feladatok:
    output = feladat[1].finish()
    if not override:
        if out:
            out += "\n\n"
        out += f"{feladat[0]}.feladat\n{output}"
    else:
        with open(f"output/feladat{feladat[0]}.txt", "w", encoding="UTF-8") as f:
            f.write(f"{feladat[0]}.feladat\n{output}")

if out:
    with open(f"output/Valasz{road_code}.txt", "w", encoding="UTF-8") as f:
        f.write(out)
