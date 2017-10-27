def merge(numbers, l, m, r):

	n1 = m - 1 + 1
	n2 = r - m

	# temp
	L = [0] * (n1)
	R = [0] * (n2)

	for i in range (0, n1):
		# TODO: copy data to temp array L[]

	for i in range(0, n2):
		# TODO: copy data to temp array R[]

	i = 0		# initial index of first subarray
	j = 0		# initial index of second subarray
	k = l 	# initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			# TODO: set array index k equal to L[i]
		else:
			# TODO: set array index k equal to R[j]
		k += 1

	while i < n1:
			# TODO: copy remaining elements of L[] into numbers[k]
			# TODO: increment k and i

	while j < n2:
			# TODO: copy remaining elements of R[] into numbers[k]
			# TODO: increment k and j

def mergesort(numbers, l, r):

	if l < r:

		# find middle point
		m = (l+r)/2

		# TODO: sort first and second halves


		merge(numbers, l, m, r)

	return numbers;
