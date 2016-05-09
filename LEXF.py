with open("kmers_lex.in", "r") as f:
	letters = f.readline().strip().split(" ")
	length = int(f.readline())

current_numbers = [0] * length

while True:
	pos = length - 1
	while current_numbers[pos] > len(letters) - 1:
		for shift_pos in range(pos, length):
			current_numbers[shift_pos] = 0
		pos -= 1
		current_numbers[pos] += 1
		
	string = ""
	for number in current_numbers:
		string += letters[number]

	print string
	current_numbers[length - 1] += 1

	if sum(current_numbers) == length * len(letters) - 1:
		break
