import constants

on_all = {}
lines = []


def run(read, i):
    if read.t == "sz":
        l = read.t + "_" + read.code + "_" + read.license
        if not l in on_all:
            on_all[l] = {}
        if read.thing == "A":
            on_all[l]["A"] = read.seconds
        elif read.thing == "B":
            on_all[l]["B"] = read.seconds
        elif read.thing == "C":
            on_all[l]["C"] = read.seconds
        things = list(on_all[l].keys())
        for p in things[:-1]:
            xth = things.index(p)
            distance = constants.POSITIONS_ABC[things[xth+1]] - constants.POSITIONS_ABC[things[xth]]
            time_diff = on_all[l][things[xth+1]] - on_all[l][things[xth]]
            avg_speed = distance/time_diff*3600
            if avg_speed > constants.MAX_MOTOR:
                if " ".join([read.code, read.license, things[xth], things[xth+1], str(round(avg_speed))]) not in lines:
                    lines.append(" ".join([read.code, read.license, things[xth], things[xth+1], str(round(avg_speed))]))


def finish():
    for l in lines:
        print(l)
    return "\n".join(lines)
