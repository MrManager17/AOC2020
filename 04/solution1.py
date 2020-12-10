with open('input', 'r') as f:
	input = f.read().split('\n\n')

total_verified = 0
total = 0
for passport in input:
	passlines = passport.split('\n')
	passport_clean = {}
	for line in passlines:
		kv_pairs = line.split(' ')
		for kv in kv_pairs:
			if len(kv) < 2:
				continue
			key, value = kv.split(':')
			passport_clean[key] = value
	req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	valid = True
	optional_seen = False
	req_keys_seen = []
	for key in passport_clean:
		if key in req_keys and key not in req_keys_seen:
			req_keys_seen.append(key)
		elif key == 'cid' and not optional_seen:
			optional_seen == True
		else:
			valid = False
	if len(req_keys_seen) != len(req_keys):
		valid = False
	if valid:
		total_verified += 1
	total += 1
print(f"Total: {total}")
print(f"Total Verified: {total_verified}")
