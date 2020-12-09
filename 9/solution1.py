with open('input', 'r') as f:
	input = f.readlines()

cinput = []
for line in input:
	num = int(line.strip())
	cinput.append(num)

# I know this is not elegant, but I'm sleepy
for i in range(25,len(cinput)):
	valid = False
	for j in cinput[i-25:i]:
		for k in cinput[i-25:i]:
			if j + k == cinput[i]:
				valid = True
	if not valid:
		print(f"First: {cinput[i]}")
		break
