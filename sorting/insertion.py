def insertion(numbers):
	for i in range(1, len(numbers)):
		j = i
		while j > 0 and numbers[j-1] > numbers[j]:
                        numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
                        j -= 1
	return numbers
