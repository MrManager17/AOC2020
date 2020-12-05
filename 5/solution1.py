def find_row(value):
	bin_list = [x == "B" for x in value]
	bin_list.reverse()

	total = 0
	for x, val in enumerate(bin_list):
		total += 2**x * int(val)
	return total



def find_col(value):
	bin_list = [x == "R" for x in value]
	bin_list.reverse()
	total =  0
	for x, val in enumerate(bin_list):
		total += 2**x * int(val)
	return total


with open('input', 'r') as f:
	input = f.readlines()

seat_ids = []

for line in input:
	line = line.strip()
	row = find_row(line[:7])
	col = find_col(line[7:])
	seat_ids.append(row * 8 + col)

print(f"Max Seat ID: {max(seat_ids)}")
