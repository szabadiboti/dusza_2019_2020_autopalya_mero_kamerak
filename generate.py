import random
felseg_jel = ["AFG", "AL", "DZ", "USA", "AND", "AN", "ATG", "RA", "AUS", "A", "AZ", "BS", "BRN", "BD", "BDS", "B", "BZ", "DY", "BHUTAN", "RGB", "BOL", "BIH", "RB", "BR", "BG", "BF", "RU", "RCH", "CY", "CMR", "CR", "TCH", "CZ", "DK", "ZA", "ROK", "WD", "DOM", "DJ", "EC", "RGE", "UAE", "ET", "CI", "ER", "DPR", "CY", "EST", "ETH", "BY", "FJI", "FIN", "F", "RP", "G", "WAG", "GH", "GR", "WG", "GE", "GCA", "RG", "GUY", "RH", "NL", "HN", "HR", "IND", "RI", "IRQ", "IR", "IRL", "IS", "IL", "JA", "J", "YAR", "HKJ", "K", "CAM", "CDN", "Q", "KZ", "TMP", "EAK", "PRC", "KS", "KIR", "CO", "RCB", "CGO", "RCA", "C", "KWT", "LAO", "PL", "LS",
              "LV", "RL", "LB", "LAR", "FL", "LT", "L", "MK", "RM", "H", "MAL", "MW", "MDV", "RMM", "M", "MA", "MHL", "RIM", "MS", "MEX", "MYA", "FSM", "MD", "MC", "MGL", "MNE", "MOC", "GB", "NAM", "NAU", "D", "NEP", "NIC", "RN", "NGR", "N", "WSA", "I", "O", "RUS", "AM", "PK", "PAL", "PS", "PA", "PNG", "PY", "PE", "P", "RO", "RWA", "SCN", "WL", "WV", "SOL", "ES", "RSM", "STP", "SY", "WAL", "E", "CL", "SME", "CH", "S", "WS", "SA", "SN", "SRB", "SGP", "SYR", "SK", "SLO", "SO", "RSL", "SUD", "SD", "TJ", "RC", "EAT", "T", "TG", "TK", "TGA", "TR", "TT", "TN", "TV", "TM", "EAU", "NZ", "UA", "ROU", "UZ", "VAN", "V", "YV", "VN", "Z", "ZW", "CV"]
veichle_type = ["sz", "sz", "sz", "sz", "sz", "m", "m", "b", "b", "t", "t", "t", "t", "mk"]
abc = [chr(x) for x in range(65, 65+26)]
plates = []
for i in range(500):
    p = ""
    if i % 5 == 0:
        for j in range(3):
            p += random.choice(abc)
        p += "-"
        for j in range(3):
            p += str(random.randrange(0, 9))
    elif i % 5 == 1:
        for j in range(2):
            p += random.choice(abc)
        p += "-"
        for j in range(7):
            p += str(random.randrange(0, 9))
    elif i % 5 == 2:
        for j in range(4):
            p += random.choice(abc)
        p += "-"
        for j in range(4):
            p += str(random.randrange(0, 9))
    elif i % 5 == 3:
        for j in range(6):
            p += random.choice(abc)
        p += "-"
        for j in range(3):
            p += str(random.randrange(0, 9))
    elif i % 5 == 4:
        for j in range(4):
            p += random.choice(abc)
        p += "-"
        for j in range(4):
            p += str(random.randrange(0, 9))
    plates.append(p)

# print(plates)
start_time = [0, 0, 0]
generated = ""
length = 999
for k in range(length):
    sign = random.choice(felseg_jel)
    plt = random.choice(plates)
    if k < length/3:
        point = "A"
    if k >= length/3 and k < length/3*2:
        point = "B"
    if k >= length/3*2 and k < length:
        point = "C"
    typ = random.choice(veichle_type)
    speed = str(random.randrange(70, 180))
    plus_time_sec = random.randrange(1, 45)
    plus_time_min = 0
    start_time[2] += plus_time_sec
    if start_time[2] >= 60:
        start_time[1] += 1
        start_time[2] -= 60
    start_time[1] += plus_time_min
    if start_time[1] >= 60:
        start_time[0] += 1
        start_time[1] -= 60
    start_time_str = []
    for t in start_time:
        if len(str(t)) < 2:
            start_time_str.append("0" + str(t))
        else:
            start_time_str.append(str(t))
    start_time_str.reverse()
    time = ":".join(start_time_str)
    line = ",".join([sign, plt, point, typ, speed, time])
    generated += line + "\n"

start_distance = 0
distances = []
for i in range(3):
    start_distance += random.randrange(0, 1000)
    distances.append(start_distance)

with open("./input/M1.txt", "w") as file:
    file.write(",".join(list(map(str, distances))) + "\n")
    file.write(generated)
