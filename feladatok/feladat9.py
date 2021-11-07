import re

regex = re.compile("[A-Z]{3}-\d{3}")

infractions = []


def run(read, i):
    if read.code == 'H' and not regex.match(read.license):
        infractions.append(read.license)


def finish():
    return '\n'.join(infractions)
