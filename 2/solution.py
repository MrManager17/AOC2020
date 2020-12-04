
input = []
with open('input', 'r') as f:
	input = f.readlines();

overall = 0
for line in input:
	count, password = line.split(":")
	lower_upper = count.split(" ")[0]
	lower = lower_upper.split('-')[0]
	upper = lower_upper.split('-')[1]
	lower = int(lower)
	upper = int(upper)
	character = count.split(" ")[1]
	count = 0
	for i in password:
		if character == i:
			count += 1
	if count >= lower and count <= upper:
		overall += 1

print(overall)
