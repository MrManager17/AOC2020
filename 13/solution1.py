with open('input', 'r') as f:
	input = f.read().splitlines()

time = int(input[0])

input = [int(y) for y in list(filter(lambda x: x != 'x', input[1].split(',')))]

output = []

for i, x in enumerate(input):
	output.append(x - (time % x))

mindex = min(range(len(output)), key=output.__getitem__)

answer = output[mindex] * input[mindex]

print(f'Answer: {answer}')
