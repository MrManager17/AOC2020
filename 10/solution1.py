with open('input', 'r') as f:
	input = f.readlines()

cinput = []
for line in input:
	cinput.append(int(line.strip()))
cinput.sort()
cinput.reverse()

# Add one to the start and finish for plug + builtin adapter
total = [0,1,0,1]

for x in range(1, len(cinput)):
	diff = cinput[x] - cinput[x-1]
	total[diff] += 1

print(f'Answer = {total[1]*total[3]}')
