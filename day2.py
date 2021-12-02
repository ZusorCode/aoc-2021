from aocd import lines, submit

instructions = [(x.split()[0], int(x.split()[1])) for x in lines]

h = 0
d = 0

for instruction in instructions:
    match instruction:
        case "forward", x:
            h += x
        case "down", x:
            d += x
        case "up", x:
            d -= x
submit(h*d)


h = 0
d = 0
a = 0
for instruction in instructions:
    match instruction:
        case "forward", x:
            h += x
            d += a * x
        case "down", x:
            a += x
        case "up", x:
            a -= x

submit(h*d)