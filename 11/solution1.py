import copy

def get_adjacent(x, y, input_list):
	adjacent = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == 0 and j == 0:
				continue
			if x+i < 0 or x+i >= len(input_list):
				continue
			if y+j < 0 or y+j >= len(input_list[0]):
				continue
			adjacent.append(input_list[x + i][y + j])
	return adjacent

def main(input):
	not_changed = True
	while not_changed:
		not_changed = False
		new_input = copy.deepcopy(input)
		for x in range(len(input)):
			for y in range(len(input[0])):
				adjacent = get_adjacent(x, y, input)
				if input[x][y] == '.':
					continue
				elif input[x][y] == "L":
					if not any([x == '#' for x in adjacent]):
						new_input[x][y] = "#"
						not_changed = True
				elif input[x][y] == '#':
					if sum([x == '#' for x in adjacent]) >= 4:
						new_input[x][y] = 'L'
						not_changed = True
		input = copy.deepcopy(new_input)
	total = 0
	for line in input:
		total += sum([x == "#" for x in line])

	print(f"Total occupied: {total}")

if __name__ == "__main__":
	with open('input', 'r') as f:
		dinput = f.read().splitlines()

	cinput = []
	for line in dinput:
		cinput.append(list(line))
	main(copy.deepcopy(cinput))
	print("Done!")
