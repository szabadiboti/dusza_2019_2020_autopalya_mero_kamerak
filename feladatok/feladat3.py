import constants

veichles = []


def run(read, line_id):
    global veichles
    max_speed = 0
    exceed = False
    exceeded_str = "nem _lépte _túl"
    t = ""
    code = ""
    lcns = ""
    time_str = ""
    if read.thing == "C":
        if read.speed > max_speed:
            veichles = []
        if read.speed >= max_speed:
            max_speed = read.speed
            t, code, lcns = (read.t, read.code, read.license)
            max_allowed_speed = 0
            if t == "sz" and t == "m":
                max_allowed_speed = constants.MAX_MOTOR
            elif t == "b":
                max_allowed_speed = constants.MAX_BUS
            elif t == "t":
                max_allowed_speed = constants.MAX_TRUCK
            elif t == "mk":
                max_allowed_speed = constants.MAX_SPECIAL

            exceeded = read.speed > max_allowed_speed

            exceeds_str = "túllépte" if exceeded else "nem _lépte _túl"
            time_str = ":".join(list(map(str, [read.date.hour, read.date.minute, read.date.second])))
            veichles.append(" ".join([str(max_speed), exceeded_str, t, code, lcns, time_str]))


def finish():
    rtrn = ""
    for v in veichles:
        rtrn += v + "\n"
    rtrn = rtrn[0: -2]
    return rtrn
