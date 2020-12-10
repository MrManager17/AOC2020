with open('input', 'r') as f:
	input = f.readlines()

# Clean the input a bit
input_clean = []

for line in input:
	outer_bag, inner_bags = line.split("contain")
	outer_bag = outer_bag.strip()
	outer_bag = outer_bag.rstrip('bags')
	inner_bags = inner_bags.strip()
	input_clean.append((outer_bag, inner_bags))


to_check = ['shiny gold']

bags = set()
while len(to_check) > 0:
	item = to_check[0]
	for line in input_clean:
		outer_bag, inner_bags = line
		if item in inner_bags:
			to_check.append(outer_bag)
			bags.add(outer_bag)
	to_check.remove(item)

print(f"Total: {len(bags)}")
