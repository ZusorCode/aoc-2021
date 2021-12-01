from aocd import numbers, submit

count = 0
for i, num in enumerate(numbers):
    if i == 0:
        continue
    elif num > numbers[i - 1]:
        count += 1

print(count)
submit(count)


sums = []
count2 = 0

for i, num in enumerate(numbers):
    if i + 2 < len(numbers):
        val = num + numbers[i + 1] + numbers[i + 2]
        sums.append(val)

for i, num in enumerate(sums):
    if i == 0:
        continue
    elif num > sums[i - 1]:
        count2 += 1
print(count2)

submit(count2)