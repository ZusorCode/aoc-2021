from aocd import lines, submit
from collections import Counter


gamma = "0b"
epsilon = "0b"

for i in range(len(lines[1])):
    occurrence = Counter([line[i] for line in lines])
    gamma += occurrence.most_common()[0][0]
    epsilon += occurrence.most_common()[-1][0]

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(f"gamma {gamma} * epsilon {epsilon} = {gamma*epsilon} ")


oxy_lines = lines.copy()
co2_lines = lines.copy()

for i in range(len(lines[1])):
    oxy_lines = [line for line in oxy_lines if line[i] == Counter([line[i] for line in oxy_lines]).most_common()[0][0]]
    co2_lines = [line for line in co2_lines if line[i] == Counter([line[i] for line in co2_lines]).most_common()[-1][0]]

oxy = int(f"0b{oxy_lines[0]}", 2)
co2 = int(f"0b{co2_lines[0]}", 2)

print(f"oxygen {oxy} * co2 {co2} = {oxy*co2}")