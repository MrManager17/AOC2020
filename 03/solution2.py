
with open('input', 'r') as f:
	input = f.readlines()

index = 0
total = 0
totals = []
slopes = [1, 3, 5, 7]
for slope in slopes:
	total = 0
	index = 0
	for number, line in enumerate(input):
		line = line.strip()
		if number == 0:
			index += slope
			continue
		if line[index % len(line)] == "#":
			total += 1
		index += slope
	totals.append(total)
print(totals)
mult = 1
for i in totals:
	mult = mult * i

total = 0
index = 0
for number, line in enumerate(input):
	if number % 2 == 1:
		continue
	line = line.strip()
	if number == 0:
		index += 1
		continue
	if line[index % len(line)] == "#":
		total += 1
	index += 1


print(mult)
print(total * mult)

