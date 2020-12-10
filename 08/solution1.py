with open('input', 'r') as f:
	input = f.readlines()

clean_input = []
for line in input:
	comm, val = line.split(" ")
	clean_input.append((comm, int(val.strip())))

acc = 0
index = 0
seen = []

while index not in seen:
	seen.append(index)
	comm, val = clean_input[index]

	if comm == 'nop':
		index += 1
	elif comm == "acc":
		index += 1
		acc += val
	elif comm == "jmp":
		index += val

print(f"Command {index} was about to be executed twice!")
print(f"Accumulator = {acc}")
