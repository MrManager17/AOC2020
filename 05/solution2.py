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

max_seat = "BBBBBBBRRR"

max_seat_id = find_row(max_seat[:7]) * 8 + find_col(max_seat[7:])

full_seats = set(range(0, max_seat_id))

my_seats = set(seat_ids)

print(f"Overall max: {max_seat_id}")

empty_seats = full_seats.difference(my_seats)

prev_seat = -1
for seat in empty_seats:
	if seat - 1 == prev_seat:
		prev_seat = seat
		continue
	else:
		print(f"My seat is {seat}")
		break







