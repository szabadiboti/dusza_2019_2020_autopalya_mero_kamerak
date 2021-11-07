licenses = []
huns = 0


def run(read, i):
    global huns
    if read.code == "H" and read.license not in licenses:
        licenses.append(read.license)
        huns += 1


def finish():
    return huns
