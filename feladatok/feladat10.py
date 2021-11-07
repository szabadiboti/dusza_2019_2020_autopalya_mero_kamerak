data = {
    'személyautók': 0,
    'motorok': 0,
    'buszok': 0,
    'teherautók': 0
}

m = {
    'sz': 'személyautók',
    'mk': 'személyautók',
    'm': 'motorok',
    'b': 'buszok',
    't': 'teherautók'
}

first_check = ""
first_speed = 0
last_check = ""
last_speed = 0


def run(read, i):
    global first_check, first_speed, last_check, last_speed
    if not first_check:
        first_check = read.time
        first_speed = read.speed
    data[m[read.t]] += 1
    last_check = read.time
    last_speed = read.speed


def finish():
    s = "Kiegészítés #1:"
    for t, n in data.items():
        s += f'\n{t} száma: {n}'
    s += "\n\nKiegészítés #2:"
    s += f"\nElső mért sebesség: {first_check} - {first_speed}\nUtolsó mért sebesség: {last_check} - {last_speed}"
    return s
