
input = []
with open('input', 'r') as f:
	input = f.readlines();

overall = 0
first = False
last = False
for line in input:
	if first != last:
		overall += 1
	count, password = line.split(":")
	lower_upper = count.split(" ")[0]
	lower = lower_upper.split('-')[0]
	upper = lower_upper.split('-')[1]
	lower = int(lower)
	upper = int(upper)
	character = count.split(" ")[1]
	count = 0
	first = False
	last = False
	for x, i in enumerate(password):
		if x == lower and i == character:
			first = True
		if x == upper and i == character:
			last = True
		

print(overall)
