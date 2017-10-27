def insertion(numbers):

	for i in range(1, len(numbers)):
		key = numbers[i]

		j = i-1
		while j >= 0 and key < numbers[j]:
			# move ahead of their current position
            if numbers[j] > key:
                numbers[j-i] = numbers[j]
			
            j = j -1

		numbers[j+1] = key

	return numbers;
