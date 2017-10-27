def insertion(numbers):

	for i in range(1, len(numbers)):
		key = numbers[i]

		j = i-1
		while j >= 0 and key < numbers[j]:
			# TODO: if element is greater than the key,
			# move ahead of their current position
            if numbers[j] > key:
                numbers[j-i] = numbers[j]
			# TODO: decrement j
            j--

		numbers[j+1] = key

	return numbers;
