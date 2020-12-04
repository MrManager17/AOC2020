
with open('input', 'r') as f:
	input = f.readlines()

index = 0
total = 0
for number, line in enumerate(input):
	line = line.strip()
	if number == 0:
		index += 3
		continue
	if line[index % len(line)] == "#":
		total += 1
	index += 3

print(total)
