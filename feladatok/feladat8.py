from constants import MAX_MOTOR

who = input("Ki használja engedély nélkül a megkülönböztető jelzést?\n> ")
exists = False
infraction = "nem_szerepel"


def run(read, i):
    global infraction, exists
    if read.license == who:
        exists = True
        if infraction != "túllépte" and read.speed < MAX_MOTOR:
            infraction = "nem_lépte_túl"
        if read.speed > MAX_MOTOR:
            infraction = "túllépte"


def finish():
    if not exists:
        return "nem_szerepel"
    return f"szerepel {infraction}"
